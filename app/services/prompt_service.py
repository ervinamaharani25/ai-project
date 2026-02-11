def build_prompt(ticket: str, kb_results: list) -> str:

    kb_text = "\n".join(
        f"- {r['content']}" for r in kb_results
    )

    return f"""
You are an IT Helpdesk expert.

Ticket:
{ticket}

Knowledge Base:
{kb_text}

Respond ONLY in valid JSON:
{{
  "recommendation": "...",
  "confidence": 0.0
}}
"""