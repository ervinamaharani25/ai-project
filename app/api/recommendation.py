from fastapi import APIRouter
from app.models.request import HelpdeskRequest
from app.models.response import HelpdeskResponse, SolutionItem
from app.services.embedding_service import embed_text
from app.services.kb_service import search_kb
from app.services.llm_service import summarize_solutions

router = APIRouter(prefix="/ai/helpdesk", tags=["AI Helpdesk"])


SIMILARITY_THRESHOLD = 0.1


def pick_valid_kb_results(kb_results, threshold):
    """
    Filter KB results by similarity threshold.
    Supports both 'score' and 'distance'.
    """
    valid_results = []

    for r in kb_results:
        score = r.get("score")
        if score is None:
            score = r.get("distance")

        if score is None:
            continue

        if score >= threshold:
            valid_results.append(r)

    return valid_results


@router.post("/recommendation", response_model=HelpdeskResponse)
def get_recommendation(req: HelpdeskRequest):

    issue_text = req.description

    # 1️⃣ Embed issue
    vector = embed_text(issue_text)
    print("📏 embed dim:", len(vector))

    # 2️⃣ Search KB
    kb_results = search_kb(vector, limit=3)

    
    # print("🧠 KB_RESULTS (raw):", kb_results)
    # print("🧠 KB_RESULTS len:", len(kb_results))

    # 🔍 Debug (remove later if needed)
    print("[DEBUG] Raw KB results:", kb_results)

    # 3️⃣ Apply similarity threshold
    kb_results = pick_valid_kb_results(kb_results, SIMILARITY_THRESHOLD)

    # 4️⃣ Fallback if no valid KB match
    if not kb_results:
        return HelpdeskResponse(
            ticket_number=req.ticket_number,
            issue=issue_text,
            solutions=[
                SolutionItem(
                    solution=(
                        "No matching knowledge base found. "
                        "Please escalate this ticket to the support team for further investigation."
                    ),
                    confidence="100%"
                )
            ]
        )

    # 5️⃣ Merge KB contents
    kb_contents = [r.get("content", "") for r in kb_results if r.get("content")]

    # 6️⃣ Summarize with LLM
    final_solution = summarize_solutions(
        issue=issue_text,
        kb_contents=kb_contents
    )

    return HelpdeskResponse(
        ticket_number=req.ticket_number,
        issue=issue_text,
        solutions=[
            SolutionItem(
                solution=final_solution,
                confidence="100%"
            )
        ]
    )