import http.client
import json
from app.core.config import settings

def embed_text(text: str) -> list:
    conn = http.client.HTTPConnection(settings.OLLAMA_HOST, settings.OLLAMA_PORT)

    payload = json.dumps({
        "model": settings.OLLAMA_EMBED_MODEL,
        "prompt": text
    })

    headers = {"Content-Type": "application/json"}
    conn.request("POST", "/api/embeddings", payload, headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode())

    return data["embedding"]