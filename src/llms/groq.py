from src.core.config import settings
from langchain_groq import ChatGroq

groq_llm = ChatGroq(
    model="llama3-8b-8192",
    api_key=settings.GROQ_API_KEY,
    temperature=0,
)
