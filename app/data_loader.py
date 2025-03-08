import os
import kaggle
import pandas as pd

# Paths
DATASET = "mrsimple07/energy-consumption-prediction"
DATA_DIR = "data"
DATA_PATH = f"{DATA_DIR}/Energy_consumption.csv"

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

# only run directly, not from outside this file
if __name__ == "__main__":
    download_kaggle_dataset()
    df = load_dataset()
    df = preprocess_data(df)
    print(df.head())
    print(df.dtypes)
