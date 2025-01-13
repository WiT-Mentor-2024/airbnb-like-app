from sqlmodel import SQLModel
from database import engine


def drop_tables():
    SQLModel.metadata.drop_all(engine)


if __name__ == "__main__":
    drop_tables()
    print("All tables dropped successfully")
