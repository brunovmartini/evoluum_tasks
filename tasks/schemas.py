from typing import Optional

from pydantic import BaseModel


class TaskRequest(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class TaskResponse(TaskRequest):
    id: Optional[int] = None
    user_id: Optional[int]
