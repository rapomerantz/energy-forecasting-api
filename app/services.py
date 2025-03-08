import pandas as pd
from app.storage import load_model

model = load_model()

def predict_energy(data: dict):
    """Converts input data to DataFrame and makes a prediction."""
    if model is None:
        return {"error": "Model is not loaded"}

    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]
    return {"predicted_energy_consumption": prediction}