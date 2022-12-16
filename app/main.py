from fastapi import FastAPI

from app.api.api import api_router
from app.train import TrainClass



app = FastAPI(title="Wine Quality Prediction")

wineModel = TrainClass('base')
print('Model loaded')


app.include_router(api_router, prefix="/api")



# @app.on_event("startup")
# def init_model():
#     global wineModel