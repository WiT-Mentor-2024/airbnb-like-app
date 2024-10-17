from sqlmodel import SQLModel, create_engine, text
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL, echo=True
)  # Функция создает объект engine, который является основным интерфейсом для взаимодействия с базой данных, echo=True: включает вывод SQL-запросов в консоль для отладки

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)  # Функция создает класс серии для взаимодействия с базой данных, изменения не будут автоматически подтверждены (committed) или сбрасываться (flushed)


def check_tables():
    session = SessionLocal()  # Создаем сессию
    try:
        result = session.execute(
            text(
                """
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """
            )
        )  # Оборачиваем запрос в text()

        tables = [row.table_name for row in result]
        print(tables)
    except Exception as e:
        print({"error": str(e), "tables": []})
    finally:
        session.close()


if __name__ == "__main__":  # Этот код выполнится только если файл запущен напрямую.
    check_tables()
