from fastapi import FastAPI, HTTPException
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
    ticket_no: str
    title: str
    description: str


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
Title: {ticket.title}

Description:
{ticket.description}
""".strip()

        # Call RAG pipeline
        result = ask_ai(ticket.ticket_no, query)

        return result

    except Exception as e:
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=f"AI processing error: {str(e)}"
        )