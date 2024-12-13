from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.database import get_db 
from app.models import User, Ride, Booking
from app.schemas import UserCreate, UserResponse, Token, Booking as BookingSchema
from app.auth_utils import hash_password, verify_password, generate_access_token, decode_access_token

auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")



@auth_router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first() or db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username or email already registered, try different pls")
    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, email=user.email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@auth_router.post("/login", response_model=Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = generate_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}



@auth_router.get("/me", response_model=UserResponse)
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    username = payload.get("sub")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user



@auth_router.post("/rides/{ride_id}/book", response_model=BookingSchema)
def book_a_ride(
    ride_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user) 
):
    ride = db.query(Ride).filter(Ride.id == ride_id).first()
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
    
    db_booking = Booking(
        ride_id=ride_id,
        passenger_name=user.username,
    )
    ride.available_seats -= 1
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
