from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import User

from database import SessionLocal, engine

from schemas import UserCreate, UserResponse
from error_messages import EMAIL_ALREADY_REGISTERED


app = FastAPI()


def get_db() -> Session:  # получить db сессию
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def is_email_registered(db, email: str) -> bool:
    return db.query(User).filter(User.email == email).first() is not None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    if User.is_email_registered(db, user.email):
        raise HTTPException(status_code=400, detail=EMAIL_ALREADY_REGISTERED)

    new_user = User.create_user(db, user)

    return new_user
