from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class Ride(Base):
    __tablename__ = "rides"
    
    id = Column(Integer, primary_key=True, index=True)
    departure_location = Column(String, index=True)
    arrival_location = Column(String, index=True)
    departure_time = Column(DateTime)
    available_seats = Column(Integer)
    driver_name = Column(String)
    created_at = Column(DateTime, default=func.now()) 
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def dict(self):
        return {
            'id': self.id,
            'departure_location': self.departure_location,
            'arrival_location': self.arrival_location,
            'departure_time': self.departure_time,
            'available_seats': self.available_seats,
            'driver_name': self.driver_name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }