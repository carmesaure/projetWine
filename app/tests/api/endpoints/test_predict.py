from fastapi.testclient import TestClient
from app.main import app


def test_vin_parfait():
   client = TestClient(app) 

   response = client.get("/api/predict")

   content = response.json()

   assert content["message"] == "le vin parfait"

   
def test_prediction():
   client = TestClient(app) 

   data = {
      "fixed_acidity" : 7.4,
      "volatile_acidity" : 0.7,
      "citric_acid" : 0.0,
      "residual_sugar" : 1.9,
      "chlorides" : 0.076,
      "free_sulfur_dioxide" : 11.0,
      "total_sulfur_dioxide" : 34.0,
      "density" : 0.9978,
      "pH" : 3.51,
      "sulphates" : 0.56,
      "alcohol" : 9.4
   }
   

   response = client.post("/api/predict", json=data)

   content = response.json()

   assert content["quality_prediction"]