from fastapi import FastAPI
from .database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

#Create FastAPI application
app = FastAPI(
    title = "SecureTask Manager API",
    description = "A secure REST API with authentication and task management",
    version="1.0.0"
)

@app.get("/")
def health_check():
    """
    Health check endpoint to confirm API is running.
    """
    return{"status": "API is running"}