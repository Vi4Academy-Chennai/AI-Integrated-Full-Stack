# schemas.py
from pydantic import BaseModel
import datetime

# Schema for incoming prediction creation request
class PredictionCreate(BaseModel):
    feature1: float
    feature2: float

# Schema for updating an existing prediction record
class PredictionUpdate(BaseModel):
    feature1: float | None = None
    feature2: float | None = None
    prediction_result: float | None = None

# Schema for returning records to the client
class PredictionResponse(BaseModel):
    id: int
    feature1: float
    feature2: float
    prediction_result: float
    created_at: datetime.datetime

    class Config:
        from_attributes = True