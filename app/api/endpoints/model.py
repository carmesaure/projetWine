from fastapi import APIRouter

from app.api.endpoints.utils import ModelParams, Wine

router = APIRouter()



@router.get("/")
async def get_model():
    return {"message": "description du modele"}

    
    
@router.get("/description")
async def get_model_infos():
    return {"message": "infos sur le modele"}

    
@router.put("/")
async def add_wine(wine: Wine):
    return {**wine.dict()}
    

@router.post("/retrain")
async def retrain_model(params: ModelParams):
    return {**params.dict()}