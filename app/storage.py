import os
import joblib

MODEL_PATH = "models/energy_model.pkl"

def load_model():
    """Loads the trained model from disk."""
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

def save_model(model):
    """Saves the trained model to disk."""
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)