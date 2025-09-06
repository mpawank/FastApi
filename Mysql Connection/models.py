from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
  __tablename__ ="users"

  id=Column(Integer, primary_key=True, index=True)
  name = Column(String(50), index=True)
  email = Column(String(100), unique=True, index=True)
  password = Column(String(100))
  age = Column(Integer)

class Order(Base):
  __tablename__ = "orders"

  id = Column(Integer, primary_key=True, index=True)
  item_name = Column(String(100), index=True)
  quantity = Column(Integer)
  user_id = Column(Integer)  


