from typing import Union

from fastapi import FastAPI, Depends, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import User

from database import SessionLocal, engine

from schemas import UserCreate, UserResponse
from error_messages import EMAIL_ALREADY_REGISTERED
from price_generator import generate_random_price, update_prices_periodically
import asyncio
from db_utils import get_db
from fastapi.middleware.cors import CORSMiddleware
from schemas import ApartmentCreate, ApartmentResponse
from models import Apartment
from typing import Dict, Set
import json

from fastapi import APIRouter

router = APIRouter(prefix="/api")

app = FastAPI(prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


price_update_stop_event = None


active_connections: list[WebSocket] = []


subscriptions: Dict[int, Set[WebSocket]] = {}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    print(f"Client connected. Total connections: {len(active_connections)}")

    try:
        while True:

            data = await websocket.receive_text()
            print(f"Received message: {data}")

            with Session(engine) as session:
                apartments = (
                    session.query(Apartment)
                    .filter(Apartment.is_available == True)
                    .all()
                )
                updates = []

                for apartment in apartments:
                    updates.append(
                        {"id": apartment.id, "price": apartment.price_per_night}
                    )

                await websocket.send_json({"type": "price_updates", "updates": updates})

    except WebSocketDisconnect:
        active_connections.remove(websocket)
        print(f"Client disconnected. Total connections: {len(active_connections)}")


async def broadcast_price_updates():
    while True:
        if active_connections:
            with Session(engine) as session:
                apartments = (
                    session.query(Apartment)
                    .filter(Apartment.is_available == True)
                    .all()
                )
                updates = []

                for apartment in apartments:
                    updates.append(
                        {"id": apartment.id, "price": apartment.price_per_night}
                    )

                print(f"Broadcasting price updates: {updates}")

                for connection in active_connections:
                    try:
                        await connection.send_json(
                            {"type": "price_updates", "updates": updates}
                        )
                    except:
                        active_connections.remove(connection)

        await asyncio.sleep(5)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    if User.is_email_registered(db, user.email):
        raise HTTPException(status_code=400, detail=EMAIL_ALREADY_REGISTERED)

    new_user = User.create_user(db, user)

    return new_user


@router.get("/apartments/", response_model=list[ApartmentResponse])
def get_apartments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Apartment).offset(skip).limit(limit).all()


@router.post("/apartments/", response_model=ApartmentResponse)
def create_apartment(apartment: ApartmentCreate, db: Session = Depends(get_db)):
    return Apartment.create_apartment(db, apartment)


@router.get("/apartments/{apartment_id}", response_model=ApartmentResponse)
def get_apartment(apartment_id: int, db: Session = Depends(get_db)):
    apartment = db.query(Apartment).filter(Apartment.id == apartment_id).first()
    if apartment is None:
        raise HTTPException(status_code=404, detail="Apartment not found")
    return apartment


@app.on_event("startup")
async def startup_event():
    """
    Запускается при старте FastAPI приложения
    """
    stop_event = update_prices_periodically(interval_seconds=60)
    asyncio.create_task(broadcast_price_updates())


@app.on_event("shutdown")
async def shutdown_event():
    """
    Запускается при остановке FastAPI приложения
    """
    print("Shutting down price updates.")


app.include_router(router)
