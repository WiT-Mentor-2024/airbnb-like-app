from typing import Optional

from sqlmodel import Field, SQLModel

from pydantic import EmailStr


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, nullable=False, max_length=20)
    email: EmailStr = Field(index=True, nullable=False, unique=True)
    hashed_password: str = Field(nullable=False)

    role: str = Field(default="user", max_length=20)

    first_name: Optional[str] = Field(max_length=30)
    last_name: Optional[str] = Field(max_length=30)

    address: Optional[str] = Field(max_length=100)
    phone_number: Optional[str] = Field(max_length=15)
