from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Krishna!"}

@app.post("/items/")
def create_item(item:Item):
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}