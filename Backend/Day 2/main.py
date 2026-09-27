# main.py
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import PredictionRecord

# Automatically create database tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ML Backend with MySQL", version="1.0")

class PredictionInput(BaseModel):
    feature1: float
    feature2: float

@app.get("/")
def read_root():
    return {"message": "FastAPI and MySQL integration active!"}

@app.post("/predict")
def create_prediction(data: PredictionInput, db: Session = Depends(get_db)):
    # Calculate mock prediction score
    score = (data.feature1 + data.feature2) * 1.5
    
    try:
        # Create a new database record instance
        db_record = PredictionRecord(
            feature1=data.feature1,
            feature2=data.feature2,
            prediction_result=round(score, 2)
        )
        
        # Add to session, commit transaction, and refresh
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        
        return {
            "status": "success",
            "record_id": db_record.id,
            "prediction": db_record.prediction_result,
            "created_at": db_record.created_at
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/predictions")
def get_all_predictions(db: Session = Depends(get_db)):
    # Query all records from MySQL table
    records = db.query(PredictionRecord).all()
    return {"total_records": len(records), "data": records}