from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Define a Pydantic model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    class Item(BaseModel):
        name: str
        description: str | None = None
        price: float
        tax: float | None = None


@app.get("/items/", response_model=List[Item])
async def read_items():
    return list(items.values())


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id not in items:
        return {"error": "Item not found"}
    items[item_id] = item
    return item