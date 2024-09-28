from database import Base
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__="usrs.db"
    id:Column(Integer,primary_key=True)
    name:Column(String)
    email:Column(String)
    nickname:Column(String)