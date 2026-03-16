import requests
from app_v1.config import OLLAMA_URL, LLM_MODEL_2, LLM_MODEL


def generate_answer(context_chunks: list[str], question: str):

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an Apollo Helpdesk assistant.

OUTPUT FORMAT:
Here is the recommendation for troubleshooting your issue:
1. ...
2. ...
3. ...

IMPORTANT RULES:
- Use ONLY the information written in the Knowledge Base (KB).
- DO NOT use external knowledge.
- DO NOT make assumptions or infer missing information.
- Keep the wording close to the KB. Avoid excessive paraphrasing.
- Do NOT add explanations or information that are not present in the KB.
- The final answer must follow the required output format using numbered steps.
- If the answer cannot be found in the KB, respond exactly with:
  "Please contact technical IT/SDI team for the detail troubleshoot step".

TASK:
1. Identify the relevant information in the Knowledge Base that answers the question.
2. Extract the troubleshooting steps from the KB.
3. Merge and summarize them into ONE clear solution.
4. Present the solution using numbered steps.
5. Ensure the steps remain faithful to the original KB wording.

Context:
{context}

Question:
{question}
"""


    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            # "model": LLM_MODEL_2,
            "model": LLM_MODEL, #llama3 
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    # data = response.json()
    # return {
    #     "answer": data.get("response", "")
    # }

    return response.json()["response"]