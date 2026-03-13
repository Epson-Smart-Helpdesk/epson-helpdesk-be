from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Ticket(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_email: str
    subject: str
    description: str
    status: str = Field(default="open") # open, in_progress, resolved
    created_at: datetime = Field(default_factory=datetime.utcnow)