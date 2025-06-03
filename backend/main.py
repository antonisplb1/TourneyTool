# backend/main.py
from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()

# Simple test route
@app.get("/")
async def root():
    return {"message": "Hello from FastAPI backend!"}
