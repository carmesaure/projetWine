from fastapi.testclient import TestClient
from app.main import app


def test_vin_parfait():
   client = TestClient(app) 

   response = client.get("/api/predict")

   content = response.json()

   assert content["message"] == "le vin parfait"

   
   

def test_prediction():
   client = TestClient(app) 

   data = {"ph": 8.8, "sulphates": 7.6}

   response = client.post("/api/predict", json=data)

   content = response.json()

   assert content["ph"] == data["ph"]
   assert content["sulphates"] == data["sulphates"]
    