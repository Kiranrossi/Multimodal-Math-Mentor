from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY

def get_llm(temperature=0.0):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not found.")
    try:
        return ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=GROQ_API_KEY,
            temperature=temperature
        )
    except Exception as e:
        raise Exception(f"Failed to initialize ChatGroq: {e}")
