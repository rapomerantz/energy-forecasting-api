# Energy Consumption Forecasting API

This is a FastAPI-based microservice for forecasting energy consumption using machine learning.

## Features
- Accepts energy consumption data for analysis
- Provides predictions based on historical data
- Uses FastAPI for a lightweight, high-performance API

## Installation
Clone the repository and install dependencies:
```sh
git clone https://github.com/your-username/energy-forecasting-api.git
cd energy-forecasting-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the API
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoints
- `GET /` - Health check
- `POST /data` - Submit energy consumption data
- `GET /forecast` - Get energy consumption predictions

## License
MIT