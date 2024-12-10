from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from pydantic.types import conint

class RideBase(BaseModel):
    departure_location: str = Field(..., min_length=2, max_length=100)
    arrival_location: str = Field(..., min_length=2, max_length=100)
    departure_time: datetime
    available_seats: conint(ge=0, le=8)
    driver_name: str = Field(..., min_length=2, max_length=30)
    
class RideCreate(RideBase):
    """Uses all fields from RideBase, nothing more needed to add"""
    pass

class RideUpdate(BaseModel):
    departure_location: Optional[str] = Field(None, min_length=2, max_length=100)
    arrival_location: Optional[str] = Field(None, min_length=2, max_length=100)
    departure_time: Optional[datetime]
    available_seats: Optional[conint(ge=0, le=8)]
    driver_name: Optional[str] = Field(None, min_length=2, max_length=30)
    
class Ride(RideBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.strftime("%d.%m.%Y %H:%M") # Date format for JSON
        }
        
class GetRidesSchema(BaseModel):
    rides: list[Ride]
    
class BookingCreate(BaseModel):
    passenger_name: str = Field(..., min_length=2, max_length=30)
    
class Booking(BookingCreate):
    id: int
    ride_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    
    class Config:
        from_attributes = True


"""
CURRENTLY ON HOLD, IF TIME YES

class UserWithRides(BaseModel):
    id: int
    username: str
    email: EmailStr
    rides: List[Ride] = []

    class Config:
        from_attributes: = True
"""
class Token(BaseModel):
    access_token: str
    token_type: str

class tokenData(BaseModel):
    username: str | None = None
