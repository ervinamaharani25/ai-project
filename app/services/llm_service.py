import requests
from app.core.config import settings

def summarize_solutions(issue: str, kb_contents: list[str]) -> str:
    joined = "\n".join([f"- {c}" for c in kb_contents])

    prompt = f"""
You are an IT Helpdesk assistant.

Issue:
{issue}

Knowledge base solutions:
{joined}

Task:
Merge and summarize into ONE clear solution.
Use numbered steps.
Do not add new information.
"""
    url = f"{settings.OLLAMA_BASE_URL}{settings.OLLAMA_GENERATE_PATH}"

    resp = requests.post(
        url,
        json={
            "model": settings.OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )
    
    print("Status:", resp.status_code)
    print("Raw response:", resp.text)
    resp.raise_for_status()

    data = resp.json()

    print("LLM RAW RESPONSE:", data)  # temporary debug

    return data["message"]["content"].strip()