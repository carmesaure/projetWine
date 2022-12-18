from pydantic import BaseModel, Field

    
positive = Field(ge=0, description="Must be a positive value")
    
class InputWine(BaseModel):
    """Represents input data for a wine that can be added to the data file"""
    fixed_acidity : float = positive
    volatile_acidity : float = positive
    citric_acid : float = positive
    residual_sugar : float = positive
    chlorides : float = positive
    free_sulfur_dioxide : float = positive
    total_sulfur_dioxide : float = positive
    density : float = positive
    pH : float = positive
    sulphates : float = positive
    alcohol : float = positive
    quality : int = Field(ge=0, le=10, description="Quality value must be between 0 and 10")

    
class InputWinePredict(BaseModel):
    """Represents input data for a wine given to the model to make a prediction about its quality"""
    fixed_acidity : float = positive
    volatile_acidity : float = positive
    citric_acid : float = positive
    residual_sugar : float = positive
    chlorides : float = positive
    free_sulfur_dioxide : float = positive
    total_sulfur_dioxide : float = positive
    density : float = positive
    pH : float = positive
    sulphates : float = positive
    alcohol : float = positive