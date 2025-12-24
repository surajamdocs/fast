from fastapi import FastAPI, HTTPException
from models import Item

app = FastAPI()

items = []

@app.get("/")
def read_root():
    print("change 1")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
