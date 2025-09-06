from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    age: int

class UserCreate(UserBase):
  pass

class UserOut(UserBase):
   id: int

   class Config:
      orm_mode = True
   


