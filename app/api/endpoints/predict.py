from fastapi import APIRouter

from app.api.endpoints.utils import InputWinePredict
import app.main as main


router = APIRouter()



@router.get("/")
async def vin_parfait():
    return {"message" : "le vin parfait"}
    
    
@router.post("/")
async def prediction(wine: InputWinePredict):
    """Gives the model's prediction about a wine's quality given some input wine data

    Args:
        wine (InputWinePredict): Input wine data for the prediction

    Returns:
        Dict[str, float]: The quality value predicted by the model
    """
    data = [list(wine.__dict__.values())]
    prediction = main.wineModel.model.predict(data)
    return {"quality_prediction" : float(prediction[0][0])}