# import os

class Settings:
    # APP_NAME = os.getenv("APP_NAME", "ai-helpdesk-service")

    # OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")
    # OLLAMA_PORT = int(os.getenv("OLLAMA_PORT", 11434))
    # OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1")
    # OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

    # KB_API_HOST = os.getenv("KB_API_HOST", "localhost")
    # KB_API_PORT = int(os.getenv("KB_API_PORT", 8000))
    # KB_API_PATH = os.getenv("KB_API_PATH", "/kb/search")
    
    # MILVUS_HOST = os.getenv("MILVUS_HOST", "10.50.171.40")
    # MILVUS_PORT = int(os.getenv("MILVUS_PORT", 19530))
    # MILVUS_COLLECTION = os.getenv("MILVUS_COLLECTION", "helpdesk_kb")

    APP_NAME = "ai-helpdesk-service"

    OLLAMA_HOST = "localhost"
    OLLAMA_PORT = 11434 
    # OLLAMA_MODEL = "llama3:latest"
    OLLAMA_MODEL = "mistral:latest"
    OLLAMA_EMBED_MODEL = "nomic-embed-text:latest"
    OLLAMA_BASE_URL = "http://localhost:11434"
    OLLAMA_GENERATE_PATH = "/api/chat"

    KB_API_HOST = "localhost"
    KB_API_PORT = 8000
    KB_API_PATH = "/kb/search"
    
    MILVUS_HOST = "10.50.171.40"
    MILVUS_PORT = 19530
    MILVUS_COLLECTION = "helpdesk_kb"

settings = Settings()
