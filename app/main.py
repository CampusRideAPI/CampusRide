# backend/app/main.py
from fastapi import FastAPI
from . import models
from .database import engine
from app.auth_router import auth_router
from .api import router as api_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CampusRide API", debug=False) 
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def frontend():
    with open(Path("app/templates/index.html")) as file:
        return HTMLResponse(content=file.read())


app.include_router(api_router, prefix="/api", tags=["Rides and Bookings"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

"""@app.get("/")
def root():
    return {"message": "Welcome to CampusRide API"}"""
    