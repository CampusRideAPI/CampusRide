from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
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
        orm_mode: True
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
        orm_mode: True