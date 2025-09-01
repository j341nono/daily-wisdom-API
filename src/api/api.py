from fastapi import FastAPI
from pydantic import BaseModel
from src.database.models import (
    get_random_qoute,
    insert_qoute,
)


class Item(BaseModel):
    philosopher: str
    quote: str


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

@app.post("/quotes")
async def _post_quote(item: Item):
    try:
        insert_qoute(item.philosopher, item.quote)
        success = True
    except:
        success = False
    if success:
        return {"success": success, "message": "Quote added successfully."}
    else:
        return {"success": success, "message": "Both 'philosopher' and 'quote' are required."}

    
