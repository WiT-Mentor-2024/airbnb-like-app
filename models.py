from typing import Optional

from sqlmodel import Field, SQLModel

from pydantic import EmailStr
from utils import hash_password
from schemas import UserCreate, ApartmentCreate
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

    # Relationship with Booking model
    bookings = relationship("Booking", back_populates="user")

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


class Apartment(SQLModel, table=True):
    __tablename__ = "apartments"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str = Field()
    price_per_night: float = Field()
    location: str = Field()
    guests_number: int = Field()
    is_available: bool = Field(default=True)

    # Relationship with Booking model
    bookings = relationship("Booking", back_populates="apartment")

    @classmethod
    def create_apartment(
        cls, db: Session, apartment_data: ApartmentCreate
    ) -> "Apartment":

        new_apartment = cls(
            title=apartment_data.title,
            description=apartment_data.description,
            price_per_night=apartment_data.price_per_night,
            location=apartment_data.location,
            is_available=apartment_data.is_available,
            guests_number=apartment_data.guests_number,
        )

        db.add(new_apartment)
        db.commit()
        db.refresh(new_apartment)
        return new_apartment


class Booking(SQLModel, table=True):
    __tablename__ = "bookings"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    user_id: int = Field(foreign_key="users.id", nullable=False)
    apartment_id: int = Field(foreign_key="apartments.id", nullable=False)
    start_date: date = Field(nullable=False)
    end_date: date = Field(nullable=False)
    total_price: float = Field()
    guests_number: int = Field()

    # Relationship
    # defines a one-to-many relationship between User and Booking,
    # where each booking belongs to a user and each user can have multiple bookings
    user = relationship(
        "User", back_populates="bookings"
    )  # relationship function in SQLAlchemy is used to define how one model (table) is related to another
    apartment = relationship(
        "Apartment", back_populates="bookings"
    )  # back_populates attribute allows the relationship to be navigated from both sides

    @classmethod
    def create_booking(cls, db: Session, booking_data: BookingCreate) -> "Booking":
        new_booking = cls(**booking_data.model_dump())
        db.add(new_booking)
        db.commit()
        db.refresh(new_booking)
        return new_booking

    @classmethod
    def get_bookings_by_user(cls, db: Session, user_id: int) -> List["Booking"]:
        return db.query(cls).filter(cls.user_id == user_id).all()

    @classmethod
    def get_bookings_by_apartment(
        cls, db: Session, apartment_id: int
    ) -> List["Booking"]:
        return db.query(cls).filter(cls.apartment_id == apartment_id).all()

    @classmethod
    def get_booking_by_id(cls, db: Session, booking_id: int) -> "Booking":
        return db.query(cls).filter(cls.id == booking_id).first()
