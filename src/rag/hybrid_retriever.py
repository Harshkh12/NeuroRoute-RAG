from langchain_core.documents import Document
from typing import List
from src.rag.sparse_retriever import sparse_retriever

def deduplicate(docs: List[Document]) -> List[Document]:
    seen = set()
    unique = []
    for doc in docs:
        key = doc.page_content[:100]
        if key not in seen:
            seen.add(key)
            unique.append(doc)
    return unique

def rerank(docs: List[Document], query: str) -> List[Document]:
    """TF-based reranking — no LLM calls, CPU safe."""
    q_terms = set(query.lower().split())
    def score(d: Document) -> int:
        words = d.page_content.lower().split()
        return sum(words.count(t) for t in q_terms)
    return sorted(docs, key=score, reverse=True)

def hybrid_retrieve(
    query: str,
    dense_retriever,
    k: int = 5,
    grade_passed: bool = True,
    tavily_tool=None,
) -> List[Document]:
    # Dense (vector) retrieval
    dense_docs = dense_retriever.invoke(query)

    # Sparse (BM25) retrieval
    sparse_docs = sparse_retriever.retrieve(query, top_k=k)

    combined = deduplicate(dense_docs + sparse_docs)
    combined = rerank(combined, query)

    # Only hit web search if grading failed — not on doc count
    if not grade_passed and tavily_tool:
        web_results = tavily_tool.invoke(query)
        web_docs = [
            Document(
                page_content=r["content"],
                metadata={"source": r["url"], "type": "web"}
            )
            for r in web_results
        ]
        combined = deduplicate(combined + web_docs)

    return combined[:k + 3]   # slightly more to give grader options
