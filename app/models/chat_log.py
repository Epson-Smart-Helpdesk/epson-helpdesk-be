from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class ChatLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: str
    user_query: str
    bot_response: str
    is_resolved: bool = Field(default=False) # Untuk mengukur efektivitas self-service
    created_at: datetime = Field(default_factory=datetime.utcnow)