import requests
from app_v1.config import OLLAMA_URL, EMBED_MODEL
import numpy as np

def normalize(v):
    v = np.array(v)
    return (v / np.linalg.norm(v)).tolist()


def embed_text_batch(texts: list[str]):

    embeddings = []

    for text in texts:
        response = requests.post(
            f"{OLLAMA_URL}/api/embeddings",
            json={
                "model": EMBED_MODEL,
                "prompt": text
            }
        )

        response.raise_for_status()
        embeddings.append(response.json()["embedding"])

    return embeddings