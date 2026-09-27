# main.py
# uvicorn main:app --reload --port 8000
from fastapi import FastAPI
from fastapi import Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import predictions

# Automatically create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure ML Full-Stack Backend", version="1.0")


# Define allowed frontend origins
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# Add CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def restrict_methods(request: Request, call_next):
    if request.method not in ["GET"]:
        # Immediately return a 405 Method Not Allowed response
        from fastapi.responses import JSONResponse
        return JSONResponse(
            status_code=405, 
            content={"detail": "Only GET methods are allowed"}
        )
    
    response = await call_next(request)
    return response

    
# Include modular routers
app.include_router(predictions.router)

@app.get("/")
def read_root():
    return {"message": "Secure FastAPI backend with CORS and MySQL is running!"}