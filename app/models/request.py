from pydantic import BaseModel

class HelpdeskRequest(BaseModel):
    ticket_number: str
    description: str