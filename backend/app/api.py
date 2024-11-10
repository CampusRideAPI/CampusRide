from starlette import status
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db
from typing import Optional



router = APIRouter()
"""API ENDPOINTS"""
"""RIDE SPECIFIC ENDPOINTS"""
@router.get(
    "/rides",
    response_model=schemas.GetRidesSchema,
    status_code=status.HTTP_200_OK
)
def get_rides(limit: Optional[int] = None,
    db: Session = Depends(get_db)):
    query = db.query(models.Ride)
    if limit:
        query = query.limit(limit)
    rides = query.all()
    return {"rides": rides}


@router.post(
    "/rides",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.Ride
)
def create_ride(
    payload: schemas.RideCreate,
    db: Session = Depends(get_db)
):
    db_ride = models.Ride(**payload.model_dump())
    db.add(db_ride)
    db.commit()
    db.refresh(db_ride)
    return db_ride

@router.get(
    "/rides/{ride_id}",
    response_model=schemas.Ride,
    status_code=status.HTTP_200_OK
)

def get_ride(ride_id: int, db: Session = Depends(get_db)):
    ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Ride with ID {ride_id} not found")
    return ride

@router.put(
    "/rides/{ride_id}",
    response_model=schemas.Ride,
    status_code=status.HTTP_200_OK
)

def update_ride(
    ride_id: int,
    ride_details: schemas.RideUpdate,
    db: Session = Depends(get_db)
):
    ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ride with ID {ride_id} not found"
        )
        
    for key, value in ride_details.model_dump(exclude_unset=True).items():
        setattr(ride, key, value)
    db.commit()
    db.refresh(ride)
    return ride

@router.delete(
    "/rides/{ride_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response
)

def delete_ride(ride_id: int, db: Session = Depends(get_db)):
    ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ride with ID {ride_id} not found"
        )
    db.delete(ride)
    db.commit()
    return


"""BOOKING SPECIFIC ENDPOINTS"""

@router.post(
    "/rides/{ride_id}/book", response_model=schemas.Booking)

def book_a_ride(
    ride_id: int,
    booking: schemas.BookingCreate,
    db: Session = Depends(get_db)):
    ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ride with ID {ride_id} not found"
        )
    if ride.available_seats == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No available seats for this ride"
        )
        
    db_booking = models.Booking(
        ride_id=ride_id,
        passenger_name = booking.passenger_name
    )
    ride.available_seats -= 1
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
        
    
    