from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import models,schemas,crud    
from database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
  db= SessionLocal()
  try:
    yield db
  finally:
    db.close()  
    
@app.get("/users/", response_model=list[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/users",response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


