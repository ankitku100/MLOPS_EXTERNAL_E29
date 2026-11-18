
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import joblib

app = FastAPI(title="Ceramic Kiln Energy Prediction API")

model = joblib.load("kiln_model.pkl")

features = [
    "pottery_load",
    "temperature",
    "moisture",
    "duration",
    "insulation",
    "kiln_volume",
    "ambient_temp",
    "thermal_load_index",
    "moisture_removal_load"
]

class KilnInput(BaseModel):
    pottery_load: float = Field(gt=0, le=10000)
    temperature: float = Field(gt=0, le=2000)
    moisture: float = Field(ge=0, le=100)
    duration: float = Field(gt=0, le=100)
    insulation: float = Field(gt=0, le=1)
    kiln_volume: float = Field(gt=0, le=1000)
    ambient_temp: float = Field(ge=-50, le=60)


@app.get("/")
def home():
    return {"message": "Ceramic Kiln Energy Prediction API is running"}


@app.post("/predict")
def predict(data: KilnInput):

    values = data.model_dump()

    values["thermal_load_index"] = (
        values["pottery_load"] * values["temperature"]
    )

    values["moisture_removal_load"] = (
        values["pottery_load"] * values["moisture"] / 100
    )

    input_df = pd.DataFrame([values])[features]

    prediction = float(model.predict(input_df)[0])

    prediction = max(0, prediction)

    return {
        "predicted_energy_kwh": round(prediction, 2),
        "unit": "kWh"
    }
