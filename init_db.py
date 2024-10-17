from sqlmodel import SQLModel
from database import engine
from models import User


def create_db_and_tables():
    SQLModel.metadata.create_all(
        engine
    )  # SQLModel.metadata содержит информацию о всех моделях в проекте, create_all(engine) создает все таблицы, описанные в метаданных


if __name__ == "__main__":  # Этот код выполнится только если файл запущен напрямую.
    create_db_and_tables()
