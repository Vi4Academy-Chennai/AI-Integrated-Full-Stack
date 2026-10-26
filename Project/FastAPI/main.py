from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn

app = FastAPI(title="House Price Predictor API")

# Configure CORS to allow the Vite React app to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Default Vite port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the ML model
try:
    model = joblib.load('../ML/house_price_model.joblib')
except Exception as e:
    model = None
    print(f"Warning: Model could not be loaded. {e}")

class HouseFeatures(BaseModel):
    sqrft: float
    rooms: int
    year_built: int
    location_score: float

@app.post("/predict")
async def predict_price(features: HouseFeatures):
    if model is None:
        raise HTTPException(status_code=500, detail="Machine learning model is not loaded.")
    
    # Prepare input array for scikit-learn
    input_data = np.array([[
        features.sqrft,
        features.rooms,
        features.year_built,
        features.location_score
    ]])
    
    # Run prediction
    prediction = model.predict(input_data)[0]
    
    return {
        "predicted_price": round(prediction, 2),
        "currency": "USD"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)