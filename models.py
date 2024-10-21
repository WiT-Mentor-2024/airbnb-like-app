from typing import Optional

from sqlmodel import Field, SQLModel

from pydantic import EmailStr
from utils import hash_password
from schemas import UserCreate
from sqlalchemy.orm import Session


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

    @classmethod
    def is_email_registered(cls, db: Session, email: str) -> bool:
        return db.query(cls).filter(cls.email == email).first() is not None

    @classmethod
    def create_user(cls, db: Session, user_data: UserCreate) -> "User":
        hashed_password = hash_password(user_data.password)

        new_user = cls(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            address=user_data.address,
            phone_number=user_data.phone_number,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
