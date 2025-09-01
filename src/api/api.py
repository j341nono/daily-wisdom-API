from fastapi import FastAPI
from pydantic import BaseModel
from src.database.models import (
    get_random_qoute,
    insert_qoute,
    delete_qoute,
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
        insert_qoute(philosopher=item.philosopher, quotes=item.quote)
        return {
            "success": True, 
            "message": "Quote added successfully."
        }
    except Exception as e:
        return {
            "success": False, 
            "message": f"error occurred: {str(e)}",
        }


@app.delete("/quotes")
async def _delete_quote(item: Item):
    try: 
        deleted_rows = delete_qoute(philosopher=item.philosopher, quotes=item.quote)
        if deleted_rows > 0:
            return {
                "success": True, 
                "message": "Quote deleted successfully.", 
                "delete_rows": deleted_rows
            }
        else:
            return {
                "success": False,
                "message": "Philosopher or Quote not found.",
                "philosopher": item.philosopher,
                "quote": item.quote
            }
    except Exception as e:
        return {
            "success": False, 
            "message": f"error occurred: {str(e)}", 
        }

