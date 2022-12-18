from fastapi import APIRouter, HTTPException, status
from fastapi.responses import FileResponse
import json
from csv import writer

from app.train import TrainClass
from app.api.endpoints.utils import InputWine
import app.main as main

router = APIRouter()


@router.get("/")
async def get_model():
    """Returns the model serialization as json

    Returns:
        Dict[str, Dict]: Nested objects representing layers and parameters
    """
    model_json = main.wineModel.model.to_json()
    return json.loads(model_json)

    
    
@router.get("/description")
async def get_model_infos():
    """Returns basic informations about the model

    Returns:
        Dict[str, str]: Layers description, loss, optimizer and metric
    """
    return {"model description" : {
        "layers" : [
        "Dense layers of 11 units with the LeakyReLU activation",
        "Dense layers of 64 units with the LeakyReLU activation",
        "Dense layers of 64 units with the LeakyReLU activation",
        "Dense layers of 1 units with the linear activation"
        ],
         "loss" : "mean squared error",
         "optimizer" : "adam",
         "metric" : "mean absolute percentage"
    }}

    
@router.put("/")
async def add_wine(wine: InputWine):
    """Add a line to the database containing some wine's description

    Args:
        wine (InputWine): Informations about the wine

    Raises:
        HTTPException: If the server is unable to open the data file

    Returns:
        Dict[str, str]: Message confirming that the data has been added to the file
    """
    try:
        with open("app/data/Wines.csv", "a") as file:
            file_writer = writer(file)
            file_writer.writerow(list(wine.__dict__.values())+[0])
            file.close()
            return {"message" : "Wine data added to file"}
    except FileNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Data file not found")
        
    
    

@router.post("/retrain")
async def retrain_model():
    """Retrains the model using the data saved on disk

    Returns:
        Dict[str, str]: Message confirming that the retrain was successfull
    """
    main.wineModel._train()
    main.wineModel._save()
    return {'message' : "Model successfully retrained and saved"}