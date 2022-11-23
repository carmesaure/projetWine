from pydantic import BaseModel


class Wine(BaseModel):
    ph: float
    sulphates: float

    
class ModelParams(BaseModel):
    param1: float
    param2: float = 0.0