from pydantic import BaseSettings
from typing import Optional, Dict, Any, List
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ResuGenie"
    
    # OpenAI
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_API_BASE: Optional[str] = os.getenv("OPENAI_API_BASE")
    OPENAI_DEFAULT_MODEL: str = os.getenv("OPENAI_DEFAULT_MODEL", "gpt-3.5-turbo")
    
    # DeepSeek
    DEEPSEEK_API_KEY: Optional[str] = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_API_BASE: Optional[str] = os.getenv("DEEPSEEK_API_BASE", "https://api.deepseek.com/v1")
    DEEPSEEK_DEFAULT_MODEL: str = os.getenv("DEEPSEEK_DEFAULT_MODEL", "deepseek-chat")
    
    # Ollama
    OLLAMA_API_BASE: Optional[str] = os.getenv("OLLAMA_API_BASE", "http://localhost:11434/api")
    OLLAMA_DEFAULT_MODEL: str = os.getenv("OLLAMA_DEFAULT_MODEL", "llama2")
    
    # Available models mapping
    MODEL_PROVIDERS: Dict[str, str] = {
        "gpt-3.5-turbo": "openai",
        "gpt-4": "openai",
        "gpt-4-turbo": "openai",
        "deepseek-chat": "deepseek",
        "deepseek-coder": "deepseek",
        "llama2": "ollama",
        "mistral": "ollama",
        "gemma": "ollama",
    }

settings = Settings()
