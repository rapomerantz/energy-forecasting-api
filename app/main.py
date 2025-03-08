from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import os

# Initialize FastAPI app
app = FastAPI()

# Model path
MODEL_PATH = "models/energy_model.pkl"

# Load the trained model if it exists
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

# Define request schema
class EnergyInput(BaseModel):
    Temperature: float
    Humidity: float
    SquareFootage: float
    Occupancy: int
    HVACUsage: int
    LightingUsage: int
    RenewableEnergy: float
    DayOfWeek: int
    Holiday: int

@app.get("/")
def root():
    return {"message": "Energy Forecasting API is running"}

@app.post("/predict")
def predict_energy(data: EnergyInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded")

    # Convert request data to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Make prediction
    prediction = model.predict(input_df)[0]

    return {"predicted_energy_consumption": prediction}