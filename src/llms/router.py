from src.llms.groq import groq_llm
from src.llms.gemini import gemini_llm
import os

def select_llm(route: str):
    """
    Route:
      general → Groq
      search  → Gemini
      index   → Gemini
      verify  → Groq
    """
    preferred = {
        "general": groq_llm,
        "search": gemini_llm,
        "index": gemini_llm,
        "verify": groq_llm,
    }
    return preferred.get(route, groq_llm)

# For backward compatibility, just alias default to groq
llm = select_llm("index")
cheap_llm = groq_llm
