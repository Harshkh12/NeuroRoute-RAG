"""
Graph builder module for the adaptive RAG system.
"""

import json
from langchain_community.tools import TavilySearchResults
from langchain_core.messages import AIMessage
from langchain_core.prompts import PromptTemplate
from langgraph.constants import START, END
from langgraph.graph.state import StateGraph

from src.rag.reAct_agent import agent_executor
from src.rag.retriever_setup import get_retriever, embeddings
from src.config.settings import Config
from src.llms.router import llm, select_llm, cheap_llm
from src.models.grade import Grade
from src.models.route_identifier import RouteIdentifier
from src.models.state import State
from src.tools.graph_tools import routing_tool, doc_tool
from src.rag.hybrid_retriever import hybrid_retrieve
from langchain.retrievers.document_compressors import EmbeddingsFilter
import asyncio

config = Config()

# Node implementations
def query_classifier(state: State):
    question = state["messages"][-1].content
    retriever = get_retriever()
    
    # Actually retriever.invoke is synchronous but using qdrant or FAISS backing
    # Wait, the retriever might fail if it's FAISS without items yet
    try:
        context = retriever.invoke(question)
    except:
        context = []

    llm_with_structured_output = llm.with_structured_output(RouteIdentifier)
    classify_prompt = PromptTemplate(
        template=config.prompt("classify_prompt"),
        input_variables=["question", "context"]
    )
    chain = classify_prompt | llm_with_structured_output
    result = chain.invoke({"question": question, "context": context})

    return {"messages": state["messages"], "route": result.route, "latest_query": question}

def general_llm(state: State):
    result = llm.invoke(state["messages"])
    return {"messages": result}

async def adaptive_k_node(state: State):
    from src.db.feedback_repository import FeedbackRepository
    from src.db.mongo_client import get_db

    db = await get_db()
    repo = FeedbackRepository(db)
    avg_score = await repo.get_avg_score(state.get("latest_query", ""))

    k = 5
    if avg_score < -0.3:
        k = 10
    elif avg_score > 0.5:
        k = 3

    return {"k": k, "feedback_score": avg_score}

def retriever_node(state: State):
    k = state.get("k", 5)
    grade_passed = state.get("binary_score") != "no" # fallback for hybrid web

    tavily_tool = TavilySearchResults()
    retriever = get_retriever()

    docs = hybrid_retrieve(
        query=state.get("latest_query", ""),
        dense_retriever=retriever,
        k=k,
        grade_passed=grade_passed,
        tavily_tool=tavily_tool,
    )

    sources = []
    for doc in docs:
        meta = doc.metadata or {}
        sources.append({
            "file": meta.get("source", meta.get("filename", "unknown")),
            "page": meta.get("page", "-"),
            "type": meta.get("type", "index"),
        })

    # Join results so downstream 'grade' node gets a single text blob message
    context_text = "\n\n".join(d.page_content for d in docs)
    new_message = AIMessage(content=context_text)

    return {"messages": [new_message], "documents": docs, "sources": sources}

def context_compression_node(state: State):
    docs = state.get("documents", [])
    if not docs:
        return {}

    ef = EmbeddingsFilter(
        embeddings=embeddings,
        similarity_threshold=0.70,
    )
    
    try:
        filtered = ef.compress_documents(docs, state.get("latest_query", ""))
        final_docs = filtered if filtered else docs
    except Exception:
        final_docs = docs

    context_text = "\n\n".join(d.page_content for d in final_docs)
    new_message = AIMessage(content=context_text)

    return {"documents": final_docs, "messages": [new_message]}

def grade(state: State):
    grading_prompt = PromptTemplate(
        template=config.prompt("grading_prompt"),
        input_variables=["question", "context"]
    )
    context = state["messages"][-1].content
    question = state["latest_query"]

    # We use groq/router llm
    llm_with_grade = llm.with_structured_output(Grade)

    chain_graded = grading_prompt | llm_with_grade
    result = chain_graded.invoke({"question": question, "context": context})

    return {"messages": state["messages"], "binary_score": result.binary_score}


def rewrite_query(state: State):
    query = state["latest_query"]
    rewrite_prompt = PromptTemplate(
        template=config.prompt("rewrite_prompt"),
        input_variables=["query"]
    )
    chain = rewrite_prompt | llm
    result = chain.invoke({"query": query})

    retries = state.get("retries", 0) + 1
    return {
        "latest_query": result.content,
        "retries": retries
    }


def generate(state: State):
    context = state["messages"][-1].content
    generate_prompt = PromptTemplate(
        template=config.prompt("generate_prompt"),
        input_variables=["context"]
    )

    generate_chain = generate_prompt | llm
    result = generate_chain.invoke({"context": context})
    
    generation_text = result.content
    sources = state.get("sources", [])
    if sources:
        seen = set()
        unique_sources = []
        for s in sources:
            if s["file"] not in seen:
                seen.add(s["file"])
                unique_sources.append(s)
        source_lines = "\n".join(
            f"  • {s['file']}" + (f" (page {s['page']})" if s['page'] != "-" else "")
            for s in unique_sources
        )
        generation_text += f"\n\n**Sources:**\n{source_lines}"

    return {"messages": [{"role": "assistant", "content": generation_text}], "generation": generation_text}


def verify_node(state: State) -> State:
    docs = state.get("documents", [])
    context = "\n\n".join(d.page_content for d in docs)
    gen = state.get("generation", state["messages"][-1].content)
    
    prompt = config.prompt("verify_prompt").format(
        question=state.get("latest_query", ""),
        context=context[:3000],
        final_answer=gen,
    )

    try:
        response = cheap_llm.invoke(prompt)
        raw = response.content.strip()
        raw = raw.replace("```json", "").replace("```", "").strip()
        result_content = json.loads(raw)
        verified = result_content.get("verified", True)
    except Exception:
        verified = True

    return {"verified": verified}


def web_search(state: State):
    search_tool = TavilySearchResults()
    result = search_tool.invoke(state["latest_query"])

    contents = [item["content"] for item in result if "content" in item]

    return {
        "messages": [{"role": "assistant", "content": "\n\n".join(contents)}]
    }

def route_after_verify(state: State) -> str:
    if not state.get("verified", True):
        return "rewrite"
    return END

# Build the graph
graph = StateGraph(State)

graph.add_node("query_analysis", query_classifier)
graph.add_node("adaptive_k", adaptive_k_node)
graph.add_node("retriever", retriever_node)
graph.add_node("context_compression", context_compression_node)
graph.add_node("grade", grade)
graph.add_node("generate", generate)
graph.add_node("rewrite", rewrite_query)
graph.add_node("web_search", web_search)
graph.add_node("general_llm", general_llm)
graph.add_node("verify", verify_node)

graph.add_edge(START, "query_analysis")
graph.add_conditional_edges("query_analysis", routing_tool)

# Adaptive -> Retriever
graph.add_edge("adaptive_k", "retriever")

# Node routes
graph.add_edge("web_search", "generate")
graph.add_edge("retriever", "context_compression")
graph.add_edge("context_compression", "grade")
graph.add_conditional_edges("grade", doc_tool)

# generate -> verify
graph.add_edge("generate", "verify")
graph.add_conditional_edges("verify", route_after_verify)

graph.add_edge("rewrite", "adaptive_k") # start retrying from getting new k
graph.add_edge("general_llm", END)

builder = graph.compile()
