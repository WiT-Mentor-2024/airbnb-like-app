from sqlmodel import SQLModel
from database import engine
from models import User


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":  # Этот код выполнится только если файл запущен напрямую.
    create_db_and_tables()
