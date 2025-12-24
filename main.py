from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    print("change 1")
    print("change 2")
    print("change 3")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
