# main.py
from fastapi import FastAPI
from database import engine, Base
from routers import predictions

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Modular ML CRUD Backend", version="1.0")

# Include modular router
app.include_router(predictions.router)

@app.get("/")
def read_root():
    return {"message": "Modular FastAPI backend with full MySQL CRUD active!"}