APP_NAME = "Apollo AI Helpdesk"

# Ollama
OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3"
EMBED_MODEL_2 = "bge-m3:latest"
LLM_MODEL_2 = "qwen2:7b-instruct"

# Milvus
MILVUS_HOST = "10.50.171.40"
MILVUS_PORT = "19530"
COLLECTION_NAME = "helpdesk_kb"
COLLECTION_NAME_2 = "qwen_kb"

EMBEDDING_DIM = 768
EMBEDDING_DIM_2 = 1024
TOP_K = 2