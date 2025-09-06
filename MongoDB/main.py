from fastapi import FastAPI,APIRouter, HTTPException
from configurations import collection
from database.schemas import all_tasks, individual_data 
from database.models import Todo
app = FastAPI()

router = APIRouter()

@router.get("/")
async def get_all_todos():
  data = collection.find()
  return all_tasks(data)

@router.post("/")
async def create_task(new_task: Todo):
  try:
    resp = collection.insert_one(dict(new_task))
    return {"status_code": 200,"id":str(resp.inserted_id)}
  except Exception as e:
    return HTTPException(status_code=500, detail=f"some error occured {e}")

@router.put("/{task_id}")
async def update_task(task_id: str, updated_task: Todo):
  try:
    id = ObjectId(task_id)
    existing_doc = collection.find_one({"_id":id,"is_deleted":False})
    if existing_doc:
      resp = collection.update_one({"_id":id}, {"$set": dict(updated_task)})
      if resp.modified_count:
        return {"status_code": 200, "message": "Successfully updated"}
      else:
        return HTTPException(status_code=404, detail="Task not found")
    else:
      return HTTPException(status_code=404, detail="Task not found")
  except Exception as e:
    return HTTPException(status_code=500, detail=f"some error occured {e}")

app.include_router(router)