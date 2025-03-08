# Energy Forecasting API

## Overview
This project provides a FastAPI-based microservice for forecasting energy consumption based on various environmental and usage factors. 
It includes data preprocessing, model training, and an API for making predictions.

## Prerequisites
Ensure you have the following installed:
- Python 3.9+
- Virtual environment (recommended)
- Kaggle API credentials

## Setup Instructions

### 1. Set Up Kaggle API Key
The dataset is downloaded from Kaggle, so you need to configure your Kaggle API credentials.

1. Go to [Kaggle API](https://www.kaggle.com/account) and generate an API key.
2. Save the `kaggle.json` file to your system:
   ```sh
   mkdir -p ~/.kaggle
   mv /path/to/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   ```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Run the Data Loader
To download the dataset, preprocess it, train the model, and save it:
```sh
python app/data_loader.py
```

This will:
- Download the dataset (if not already present)
- Preprocess the data
- Train a model using Linear Regression
- Save the trained model to `models/energy_model.pkl`

### 4. Run the FastAPI Service
Start the API locally:
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Test the API
Make a prediction request:
```sh
curl -X 'POST' 'http://127.0.0.1:8000/predict' \
     -H 'Content-Type: application/json' \
     -d '{
        "Temperature": 22.5,
        "Humidity": 45.0,
        "SquareFootage": 1500.0,
        "Occupancy": 3,
        "HVACUsage": 1,
        "LightingUsage": 1,
        "RenewableEnergy": 5.0,
        "DayOfWeek": 2,
        "Holiday": 0
     }'
```

Expected response:
```json
{
    "predicted_energy_consumption": 75.3
}
```
