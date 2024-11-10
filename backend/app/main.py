# backend/app/main.py
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware FOR DEBUGGING ONLY
from . import models, api
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CampusRide API", debug=False) 


app.include_router(api.router)