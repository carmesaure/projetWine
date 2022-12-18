from fastapi import FastAPI

from app.api.api import api_router
from app.train import TrainClass



app = FastAPI(title="Wine Quality Prediction")


# Loading model 
wineModel = TrainClass('base')
print('\nModel loaded')


app.include_router(api_router, prefix="/api")