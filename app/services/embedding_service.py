import json
import requests
from app.core.config import settings


# def embed_text(text: str):
#     url = f"{settings.OLLAMA_BASE_URL}/api/embeddings"

#     resp = requests.post(
#         url,
#         json={
#             "model": settings.OLLAMA_EMBED_MODEL,
#             "prompt": text
#         },
#         timeout=60
#     )

#     print("Status:", resp.status_code)
#     print("Response:", resp.text)

#     resp.raise_for_status()

#     data = resp.json()
#     return data["embedding"]

def embed_text(text: str):
    url = "http://localhost:11434/api/embeddings"

    resp = requests.post(
        url,
        json={
            "model": "nomic-embed-text",
            "prompt": text
        },
        timeout=60
    )

    print("Status:", resp.status_code)
    print("Response JSON:", resp.json())

    resp.raise_for_status()

    return resp.json()["embedding"]