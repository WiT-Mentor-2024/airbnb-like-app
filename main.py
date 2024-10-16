from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from models import User
from utils import hash_password

from database import SessionLocal, engine


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
