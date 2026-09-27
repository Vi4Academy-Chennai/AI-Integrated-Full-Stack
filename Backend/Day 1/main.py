# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="ML Prediction Backend", version="1.0")

# Configure CORS so your React frontend (port 5173) can communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Pydantic model for incoming prediction request payloads
class PredictionInput(BaseModel):
    feature1: float
    feature2: float

# Root GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Backend for ML Predictions!"}

# POST prediction endpoint with data validation
@app.post("/predict")
def run_prediction(data: PredictionInput):
    # Simulated model inference logic (will be replaced with a .pkl model later)
    calculated_prediction = (data.feature1 + data.feature2) * 1.5
    
    return {
        "status": "success",
        "input_received": {
            "feature1": data.feature1,
            "feature2": data.feature2
        },
        "prediction": round(calculated_prediction, 2)
    }