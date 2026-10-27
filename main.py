from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/") 
def root(): 
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return item # or we can make it return the whole "items" list as well

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item
