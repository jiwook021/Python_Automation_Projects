from typing import Optional  # Allow type hints for optional parameter

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()



@app.post("/items/")
async def create_item(item: Item) -> Item:

    return item



@app.put("/items/{item_id}")
def create_items(item_id: int, item: Item, q: Optional[str] = None):
    return {"item_id": item_id, "name":item.name, "description":item.description , "price":item.price, "tax ":item.tax,"q ":q}
    
    
    
if __name__ == "__main__":
    # For debugging
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)