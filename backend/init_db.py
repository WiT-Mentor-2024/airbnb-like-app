from sqlmodel import SQLModel, Session, select
from database import engine
from models import User, Apartment
from schemas import ApartmentCreate


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        apartments = session.exec(select(Apartment)).all()
        for apt in apartments:
            session.delete(apt)
        session.commit()

        test_apartments = [
            ApartmentCreate(
                title="Cozy apartment in the center",
                description="Bright apartment with modern renovation",
                price_per_night=100.0,
                location="City Center",
                guests_number=2,
                is_available=True,
                rating=4.5,
            ),
            ApartmentCreate(
                title="Spacious apartments",
                description="Large apartment with park view",
                price_per_night=150.0,
                location="Park District",
                guests_number=4,
                is_available=True,
                rating=4.8,
            ),
            ApartmentCreate(
                title="Beach studio",
                description="Compact studio 5 minutes from the beach",
                price_per_night=80.0,
                location="Seaside District",
                guests_number=2,
                is_available=True,
                rating=4.2,
            ),
        ]

        for apartment_data in test_apartments:
            new_apartment = Apartment.create_apartment(session, apartment_data)
            print(
                f"Added apartment: {new_apartment.title} with rating {new_apartment.rating}"
            )


if __name__ == "__main__":
    create_db_and_tables()
