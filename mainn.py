from fastapi import FastAPI
from typing import Optional
from models import Base, User
from pydantic import BaseModel
from schema import UserSchema
from database import engine,Sessionlocal
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app=FastAPI()
def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()



@app.post("/adduser")
def add_user(request:UserSchema, db: Session = Depends(get_db)):
    user = User(name=request.name, email = request.email,nickname=request.nickname)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

