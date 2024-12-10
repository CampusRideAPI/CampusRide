from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Datetime
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
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
    bookings = relationship("Booking", back_populates="ride")
    
    
class Booking(Base):
    __tablename__ = "bookings"
    
    id = Column(Integer, primary_key=True, index=True)
    ride_id = Column(Integer, ForeignKey("rides.id"))
    passenger_name = Column(String)
    created_at = Column(DateTime, default=func.now())
    ride = relationship("Ride", back_populates="bookings")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(Datetime, default=datetime.utcnow)
    updated_at = Column(Datetime, default=datetime.utcnow, onupdate=datetime.utcnow)


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
