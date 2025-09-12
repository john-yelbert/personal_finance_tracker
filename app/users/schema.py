from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    profession: Optional[str] = None
    income: Optional[float] = None

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True  # allows my schema to read data from SQLAlchemy
