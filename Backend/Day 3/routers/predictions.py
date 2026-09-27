# routers/predictions.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import PredictionRecord
from schemas import PredictionCreate, PredictionUpdate, PredictionResponse
from typing import List

router = APIRouter(prefix="/predictions", tags=["Predictions CRUD"])

# 1. CREATE: Save a new prediction record
@router.post("/", response_model=PredictionResponse, status_code=status.HTTP_201_CREATED)
def create_prediction(payload: PredictionCreate, db: Session = Depends(get_db)):
    # Calculate mock ML prediction score
    score = (payload.feature1 + payload.feature2) * 1.5
    
    db_record = PredictionRecord(
        feature1=payload.feature1,
        feature2=payload.feature2,
        prediction_result=round(score, 2)
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# 2. READ: Get all prediction logs
@router.get("/", response_model=List[PredictionResponse])
def get_all_predictions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = db.query(PredictionRecord).offset(skip).limit(limit).all()
    return records

# 3. READ: Get a single prediction record by ID
@router.get("/{record_id}", response_model=PredictionResponse)
def get_prediction_by_id(record_id: int, db: Session = Depends(get_db)):
    record = db.query(PredictionRecord).filter(PredictionRecord.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Prediction record not found")
    return record

# 4. UPDATE: Modify an existing prediction record
@router.put("/{record_id}", response_model=PredictionResponse)
def update_prediction(record_id: int, payload: PredictionUpdate, db: Session = Depends(get_db)):
    record = db.query(PredictionRecord).filter(PredictionRecord.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Prediction record not found")
    
    # Update fields if provided
    if payload.feature1 is not None:
        record.feature1 = payload.feature1
    if payload.feature2 is not None:
        record.feature2 = payload.feature2
    if payload.prediction_result is not None:
        record.prediction_result = payload.prediction_result
        
    db.commit()
    db.refresh(record)
    return record

# 5. DELETE: Remove a prediction record
@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prediction(record_id: int, db: Session = Depends(get_db)):
    record = db.query(PredictionRecord).filter(PredictionRecord.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Prediction record not found")
    
    db.delete(record)
    db.commit()
    return None