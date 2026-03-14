from langchain_groq import ChatGroq
from config.config import app_config

def get_llm(temperature=0.0):
    try:
        return ChatGroq(
            model=app_config.MODEL_NAME_VERSATILE,
            api_key=app_config.GROQ_API_KEY,
            temperature=temperature
        )
    except Exception as e:
        raise Exception(f"Failed to initialize ChatGroq: {e}")
