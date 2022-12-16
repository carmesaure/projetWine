from fastapi import FastAPI

from app.api.api import api_router



app = FastAPI(title="Wine Quality Prediction")



app.include_router(api_router, prefix="/api")