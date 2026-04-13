from pydantic import BaseModel
from typing import Optional

class FeedbackRequest(BaseModel):
    query: str
    response: str
    session_id: str
    feedback: int  # +1 = helpful, -1 = not helpful
