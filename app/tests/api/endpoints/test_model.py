from fastapi.testclient import TestClient
import json
import os

import app.main as main
from app.main import app



def test_model():
   client = TestClient(app) 

   model_json = json.loads(main.wineModel.model.to_json())

   response = client.get("/api/model")
   content = response.json()

   assert content == model_json


def test_model_description():
    client = TestClient(app)

    model_json = {"model description" : {
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

    response = client.get("/api/model/description")
    content = response.json()

    assert content == model_json
    

def test_add_wine():
    client = TestClient(app)

    data = {
	"fixed_acidity" : 7.5,
    "volatile_acidity" : 0.5,
	"citric_acid" : 0.0,
	"residual_sugar" : 2.6,
	"chlorides" : 0.089,
	"free_sulfur_dioxide" : 25.0,
	"total_sulfur_dioxide" : 67.0,
	"density" : 0.999,
	"pH" : 3.3,
	"sulphates" : 0.68,
	"alcohol" : 9.8,
	"quality" : 5
    }

    # insert a data line using the api
    response = client.put("/api/model", json=data)
    content = response.json()

    expected_content = {
	    "message": "Wine data added to file"
    }

    # read this line on the file
    row = ""
    with open("app/data/Wines.csv", "r") as file:
        row = file.readlines()[-1]


    # remove last line from file now that it has been read
    with open("app/data/Wines.csv", "r+") as file:
        file.seek(0, os.SEEK_END)

        pos = file.tell() - 2

        while pos > 0 and file.read(1) != "\n":
            pos -= 1
            file.seek(pos, os.SEEK_SET)

        if pos > 0:
            file.seek(pos+1, os.SEEK_SET)
            file.truncate()


    # assert that the line read on the file corresponds to the data provided to the api
    assert (row == ','.join(map(str, list(data.values())+['0\n']))) and (content == expected_content)


def test_retrain():
    client = TestClient(app)

    model_json = {
	    "message": "Model successfully retrained and saved"
    } 

    response = client.post("/api/model/retrain")
    content = response.json()

    assert content == model_json