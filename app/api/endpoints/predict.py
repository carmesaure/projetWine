from fastapi import APIRouter

from app.api.endpoints.utils import InputWinePredict
import app.main as main


router = APIRouter()



@router.get("/")
async def vin_parfait():
    return {"message" : "le vin parfait"}
    
    
@router.post("/")
async def prediction(wine: InputWinePredict):
    data = [list(wine.__dict__.values())]
    prediction = main.wineModel.model.predict(data)
    return {"quality_prediction" : float(prediction[0][0])}