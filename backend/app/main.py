# backend/app/main.py
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware FOR DEBUGGING ONLY
from . import models, api
from .database import engine
from app.auth_router import router as auth_router
from .api import router as api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CampusRide API", debug=False) 


app.include_router(api_router, prefix="/api", tags=["Rides and Bookings"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

"""@app.get("/")
def root():
    return {"message": "Welcome to CampusRide API"}"""