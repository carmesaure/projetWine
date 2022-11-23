from fastapi import APIRouter
from app.api.endpoints.utils import Wine


router = APIRouter()



@router.get("/")
async def vin_parfait():
    return {"message": "le vin parfait"}

    
    
@router.post("/")
async def prediction(wine: Wine):
    return {**wine.dict()}