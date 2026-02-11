from pydantic import BaseModel
from typing import List

class SolutionItem(BaseModel):
    solution: str
    confidence: str = "100%"

class HelpdeskResponse(BaseModel):
    ticket_number: str
    issue: str
    solutions: List[SolutionItem]