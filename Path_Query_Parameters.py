from unittest.util import _MAX_LENGTH
from fastapi import FastAPI, Path, Query
from enum import Enum
from typing import Union


# Enum for choice names
class Choice_Names(str, Enum):
    one = "one"
    two = "two"
    three = "three"


app = FastAPI()


# Basic hello route
@app.get("/hello")
async def root():
    return {"message": "Hello from vipan side.."}


# Another route
@app.get("/hy")
async def vipan():
    return {"message": "hy, how are you!!!"}


# Path parameter with Enum
@app.get("/item/{Item}")
def path_func(Item: Choice_Names):
    var_name = {"path variable": Item}
    return var_name


# Query parameters with optional roll_no
@app.get("/query")
def query_func(
    name: str,
    roll_no: Union[int, None] = Query(default=None)
):
    var_name = {"name": name, "roll no": roll_no}
    return var_name
