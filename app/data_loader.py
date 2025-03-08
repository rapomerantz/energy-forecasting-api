import os
import kaggle
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Paths
DATASET = "mrsimple07/energy-consumption-prediction"
DATA_DIR = "data"
MODEL_DIR = "models"
DATA_PATH = f"{DATA_DIR}/Energy_consumption.csv"
MODEL_PATH = f"{MODEL_DIR}/energy_model.pkl"
# Define feature columns and target
FEATURES = [
    "Temperature", "Humidity", "SquareFootage", "Occupancy",
    "HVACUsage", "LightingUsage", "RenewableEnergy", "DayOfWeek", "Holiday"
]
TARGET = "EnergyConsumption"

def download_kaggle_dataset():
    """Downloads the dataset from Kaggle."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    kaggle.api.dataset_download_files(DATASET, path=DATA_DIR, unzip=True)
    print(f"Dataset downloaded to {DATA_DIR}")

def load_dataset():
    """Loads and previews the energy consumption dataset."""
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    # Display basic info
    print("Dataset Loaded Successfully")

    return df

def preprocess_data(df):
    """Cleans and preprocesses the dataset for forecasting."""

    # Convert Timestamp to datetime
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    # Encode binary categorical features (handling missing values safely)
    df["HVACUsage"] = df["HVACUsage"].map({"No": 0, "Yes": 1}).fillna(0).astype(int)
    df["LightingUsage"] = df["LightingUsage"].map({"No": 0, "Yes": 1}).fillna(0).astype(int)
    df["Holiday"] = df["Holiday"].map({"No": 0, "Yes": 1}).fillna(0).astype(int)

    # Encode DayOfWeek as a categorical numeric feature
    df["DayOfWeek"] = df["DayOfWeek"].astype("category").cat.codes

    # Ensure Occupancy is an integer (not float)
    df["Occupancy"] = df["Occupancy"].astype(int)

    # Ensure all other numeric columns are float
    numeric_columns = ["Temperature", "Humidity", "SquareFootage", "RenewableEnergy", "EnergyConsumption"]
    df[numeric_columns] = df[numeric_columns].astype(float)

    return df

def split_data(df):
    """Splits data into training and testing sets."""
    X = df[FEATURES]
    y = df[TARGET]

    # 80% training, 20% testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training Set Size:", X_train.shape, y_train.shape)
    print("Testing Set Size:", X_test.shape, y_test.shape)

    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """Trains a Linear Regression model on the energy dataset."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluates model performance on test data."""
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)

    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")

def save_model(model):
    """Saves the trained model to disk."""
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)

    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

# only run directly, not from outside this file
if __name__ == "__main__":
    download_kaggle_dataset()
    df = load_dataset()
    df = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(df)

    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

    save_model(model)