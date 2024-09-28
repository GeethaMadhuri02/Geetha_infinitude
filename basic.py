from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI

class Employee(BaseModel):
    id:int
    name:str
    dept:str

@app.post('/employee/')
def createEmployee(BaseModel):
    return Employee