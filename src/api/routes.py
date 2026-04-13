"""
API routes for RAG operations.
"""

from fastapi import APIRouter, UploadFile, File, Header
from fastapi.responses import StreamingResponse
from langchain_core.messages import HumanMessage, AIMessage
import json

from src.memory.chat_history_mongo import ChatHistory
from src.models.query_request import QueryRequest
from src.rag.document_upload import documents
from src.rag.graph_builder import builder
from src.models.feedback import FeedbackRequest
from src.db.feedback_repository import FeedbackRepository
from src.db.mongo_client import get_db

router = APIRouter()


@router.post("/rag/query")
async def rag_query(req: QueryRequest):
    chat_history = ChatHistory.get_session_history(req.session_id)
    await chat_history.add_message(HumanMessage(content=req.query))

    messages = await chat_history.get_messages()
    result = await builder.ainvoke({
        "messages": messages,
        "latest_query": req.query,
    })
    output_text = result["messages"][-1].content

    await chat_history.add_message(AIMessage(content=output_text))

    return {
        "result": {
            "type": "ai",
            "content": output_text,
        },
        "sources": result.get("sources", []),
    }

@router.post("/rag/stream")
async def stream_query(req: QueryRequest):
    chat_history = ChatHistory.get_session_history(req.session_id)
    await chat_history.add_message(HumanMessage(content=req.query))
    messages = await chat_history.get_messages()

    async def token_generator():
        last_generation = ""
        sources = []
        async for chunk in builder.astream(
            {"messages": messages, "latest_query": req.query}
        ):
            if "generate" in chunk:
                content = chunk["generate"].get("generation", "")
                if content:
                    last_generation = content
                    yield f"data: {json.dumps({'token': content})}\n\n"
            if "retriever" in chunk:
                sources = chunk["retriever"].get("sources", [])

        if last_generation:
            await chat_history.add_message(AIMessage(content=last_generation))
            
        yield f"data: {json.dumps({'done': True})}\n\n"

    return StreamingResponse(
        token_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )

@router.post("/rag/feedback")
async def submit_feedback(feedback: FeedbackRequest):
    db = await get_db()
    repo = FeedbackRepository(db)
    await repo.save_feedback(feedback.dict())
    return {"status": "saved"}


@router.post("/rag/documents/upload")
async def upload_file(
    file: UploadFile = File(...),
    description: str = Header(..., alias="X-Description")
):
    status_upload = documents(description, file)
    return {"status": status_upload}
