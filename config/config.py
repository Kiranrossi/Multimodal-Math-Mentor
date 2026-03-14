import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig:
    def __init__(self):
        self.GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        if not self.GROQ_API_KEY:
            raise ValueError("CRITICAL: GROQ_API_KEY environment variable is missing. Application cannot start.")
        
        self.VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH", "data/faiss_index")
        self.MODEL_NAME_VERSATILE = os.getenv("MODEL_NAME_VERSATILE", "llama-3.3-70b-versatile")
        self.MODEL_NAME_INSTANT = os.getenv("MODEL_NAME_INSTANT", "llama-3.1-8b-instant")

app_config = AppConfig()
