from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import date


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    first_name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]


class ApartmentBase(BaseModel):
    title: str
    description: str
    price_per_night: float
    location: str
    is_available: bool = True
    guests_number: int


class ApartmentCreate(ApartmentBase):
    pass


class ApartmentUpdate(ApartmentBase):
    pass


class ApartmentResponse(ApartmentBase):
    id: int


class BookingBase(BaseModel):
    start_date: date
    end_date: date
    total_price: float
    guests_number: int


class BookingCreate(BookingBase):
    user_id: int
    apartment_id: int


class BookingResponse(BookingBase):
    id: int
    user_id: int
    apartment_id: int

    class Config:
        from_attributes = True  # говорит Pydantic, что он может работать с объектами, возвращаемыми из SQLAlchemy, и преобразовывать их в формат JSON для ответа API
