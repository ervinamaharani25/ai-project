from app_v1.retriever import search_kb
from app_v1.generator import generate_answer


SIMILARITY_THRESHOLD = 0.3  # adjust later


def ask_ai(ticket_no: str, question: str) -> dict:
    """
    Full RAG pipeline for Apollo integration.
    """

    # 1️⃣ Retrieve KB results
    kb_results = search_kb(question)

    if not kb_results:
        return {
            "ticket_no": ticket_no,
            "recommendation": "No relevant knowledge base found.",
            "kb_used": [],
            "confidence_score": 0.0
        }

    # 2️⃣ Filter by similarity threshold
    filtered_results = [
        item for item in kb_results
        if item.get("score", 0) >= SIMILARITY_THRESHOLD
    ]

    if not filtered_results:
        return {
            "ticket_no": ticket_no,
            "recommendation": "No sufficiently relevant knowledge found.",
            "kb_used": [],
            "confidence_score": 0.0
        }

    # 3️⃣ Extract context
    context_chunks = [
        item.get("content")
        for item in filtered_results
        if item.get("content") is not None
    ]

    # 4️⃣ Generate answer using LLM
    answer = generate_answer(context_chunks, question)

    # 5️⃣ Confidence = highest similarity score
    top_score = max(item["score"] for item in filtered_results)

    return {
        "ticket_no": ticket_no,
        "recommendation": answer,
        "kb_used": context_chunks,
        "confidence_score": round(float(top_score), 3)
    }