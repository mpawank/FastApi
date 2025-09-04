from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/hello")
async def root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def path_func(item_id: int):
    return {"path_variable": item_id}

# GET with optional query parameters
@app.get("/query/")
async def query_func(name: Union[str, None] = None, roll_no: Union[int, "100"] = "100"):
    return {"name": name, "roll_no": roll_no}

# PUT with required query parameters
@app.put("/query/")
async def update_query(name: str, roll_no: int):
    return {"name": name, "roll_no": roll_no}
