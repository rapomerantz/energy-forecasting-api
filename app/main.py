from fastapi import FastAPI

app = FastAPI()

# Health check endpoint
@app.get("/")
def root():
    return {"message": "Energy Forecasting API is running"}

# Endpoint to submit energy usage data
@app.post("/data")
def submit_data():
    return {"message": "Data submission goes here"}

# Endpoint to get forecasted energy consumption
@app.get("/forecast")
def get_forecast():
    return {"message": "Forecasting goes here"}