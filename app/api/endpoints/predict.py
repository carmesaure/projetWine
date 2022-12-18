from fastapi import APIRouter

from app.api.endpoints.utils import InputWinePredict
import app.main as main


router = APIRouter()



@router.get("/")
async def vin_parfait():
    return {"perfect_wine" : {'fixed acidity' : 10.5,'volatile acidity': 0.3,'cytric acid':0.5,'residual sugar':2.78,'chlorides':0.071,'free sulfur dioxide':9.0,'total sulfur dioxide':16.0,'density':0.994,'pH':3.15,'sulphates':0.75,'alcohol':14}}
    
    
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