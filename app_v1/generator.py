import requests
from app_v1.config import OLLAMA_URL, LLM_MODEL


def generate_answer(context_chunks: list[str], question: str):

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an IT Helpdesk assistant.

Context:
{context}

Question:
{question}

Task:
Merge and summarize into ONE clear solution.
Use numbered steps.
Answer ONLY using the knowledge base below.
Do not add any information not present in the KB.
"""


    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": LLM_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    return response.json()["response"]