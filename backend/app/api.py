from starlette import status
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db
from typing import Optional
from .auth_utils import get_current_user
from .schemas import UserResponse as User


auth_router =APIRouter()
router = APIRouter()

"""RIDE SPECIFIC ENDPOINTS"""
@router.get(
    "/rides",
    response_model=schemas.GetRidesSchema,
    status_code=status.HTTP_200_OK
)
def get_rides(limit: Optional[int] = None,
    db: Session = Depends(get_db)):
    query = db.query(models.Ride)   # Query all rides
    if limit:
        query = query.limit(limit)  # Limit the number of rides *OPTIONAL*
    rides = query.all()     # Get all rides
    return {"rides": rides}     # Return rides list


@router.post(
    "/rides",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.Ride
)
def create_ride(
    payload: schemas.RideCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user) 
):
    db_ride = models.Ride(**payload.model_dump(), driver_id=user.id)  
    db.add(db_ride)  
    db.commit()     
    db.refresh(db_ride)   
    return db_ride 

@router.get( 
""" Returns specific ride details. """
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
    """ Update only provided fields"""
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

@auth_router.post(
    "/rides/{ride_id}/book", response_model=schemas.Booking)

def book_a_ride(
    ride_id: int,
    booking: schemas.BookingCreate,
    db: Session = Depends(get_db)):
    user=Depends(get_current_user)
    ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ride with ID {ride_id} not found"
        )
    if ride.available_seats <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No available seats for this ride"
        )
        
    db_booking = models.Booking(
        ride_id=ride_id,
        passenger_name = user  
    )
    ride.available_seats -= 1
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
        
    
