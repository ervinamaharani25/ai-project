import requests
from app_v1.config import OLLAMA_URL, EMBED_MODEL


def embed_text(text: str):
    response = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={
            "model": EMBED_MODEL,
            "prompt": text
        }
    )

    response.raise_for_status()
    return response.json()["embedding"]