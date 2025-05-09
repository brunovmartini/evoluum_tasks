from typing import Optional
from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    name: str
    last_name: str

    class Config:
        orm_mode = True


class UserRequest(UserResponse):
    password: str
