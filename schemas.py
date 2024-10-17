from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    first_name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]


class Config:
    orm_mode = True  # говорит Pydantic, что он может работать с объектами, возвращаемыми из SQLAlchemy, и преобразовывать их в формат JSON для ответа API
