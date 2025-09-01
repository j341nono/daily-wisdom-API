from fastapi import FastAPI
from src.database.models import (
    get_random_qoute,
)


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/quotes/random")
async def _get_random():
    philosopher, quote = get_random_qoute()
    return {"philosopher": philosopher, "quote": quote}

