from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel
from app_v1.rag_engine import ask_ai
import traceback


app = FastAPI(
    title="Apollo AI Service",
    version="1.0.0",
    description="AI Recommendation Service for Apollo Helpdesk"
)


# ==============================
# Request Model
# ==============================

class TicketRequest(BaseModel):
    # ticket_no: str
    title: str

# ==============================
# Health Check (Important for server)
# ==============================

@app.get("/health")
def health_check():
    return {"status": "AI service running"}


# ==============================
# AI Recommendation Endpoint
# ==============================

@app.post("/ai/recommendation")
def get_recommendation(ticket: TicketRequest):

    try:
        # Build query text for embedding
        query = f"""

title:
{ticket.title}
""".strip()

        # Call RAG pipeline
        result = ask_ai(query)
        answer_text = result.get("recommendation", "")
        answer_array = [line.strip() for line in answer_text.split("\n") if line.strip()]

        # return result
        # return answer_array
        return {
            "solution" : answer_array
        }

    except Exception as e:
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=f"AI processing error: {str(e)}"
        )