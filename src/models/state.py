"""
State model for the graph-based RAG system.
"""

from typing import TypedDict, Annotated, Optional

from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages


class State(TypedDict):
    """State schema for the RAG graph."""

    messages: Annotated[list[AnyMessage], add_messages]
    binary_score: Optional[str]
    route: Optional[str]
    latest_query: Optional[str]
    
    k: Optional[int]
    feedback_score: Optional[float]
    sources: Optional[list]
    verified: Optional[bool]
    documents: Optional[list]
    generation: Optional[str]
    retries: Optional[int]