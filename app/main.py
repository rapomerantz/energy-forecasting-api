from fastapi import FastAPI, HTTPException
from app.schemas import EnergyInput
from app.services import predict_energy

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Energy Forecasting API is running"}

@app.post("/predict")
def predict(data: EnergyInput):
    result = predict_energy(data.dict())
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result