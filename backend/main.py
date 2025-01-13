from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import User

from database import SessionLocal, engine

from schemas import UserCreate, UserResponse
from error_messages import EMAIL_ALREADY_REGISTERED
from price_generator import update_prices_periodically


app = FastAPI()

# Глобальная переменная для хранения stop_event
price_update_stop_event = None


def get_db() -> Session:  # получить db сессию
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    if User.is_email_registered(db, user.email):
        raise HTTPException(status_code=400, detail=EMAIL_ALREADY_REGISTERED)

    new_user = User.create_user(db, user)

    return new_user


@app.on_event("startup")
async def startup_event():
    """
    Запускается при старте FastAPI приложения
    """
    global price_update_stop_event
    # Запускаем обновление цен каждые 5 минут (300 секунд)
    price_update_stop_event = update_prices_periodically(300)


@app.on_event("shutdown")
async def shutdown_event():
    """
    Запускается при остановке FastAPI приложения
    """
    global price_update_stop_event
    if price_update_stop_event:
        price_update_stop_event.set()
        print("Stopping price updates...")
