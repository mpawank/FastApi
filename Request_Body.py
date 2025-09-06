from fastapi import FastAPI
from pydantic import BaseModel

class schema1(BaseModel):
    name: str
    class_name: str
    roll_no: int
    age: int

app = FastAPI()

#Request body with schema1
@app.post("/student")
async def student_info(item: schema1):
    return item