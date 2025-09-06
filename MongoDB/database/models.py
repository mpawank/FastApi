from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    is_declered: bool = False
    updated_at: int = int(datetime.timestamp(datetime.now()))
    created_at: int = int(datetime.timestamp(datetime.now()))
