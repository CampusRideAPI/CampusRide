from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import get_db



router = APIRouter()

"""API ENDPOINT TO GET ALL RIDES"""
@router.post("/rides/", response_model=List[schemas.Ride])
def get_rides(db: Session = Depends(get_db)):
    rides = crud.get_rides(db)
    return rides

"""
@router.get()
@router.post()
@router.put()
@router.delete()
"""