from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: Optional[str] = None
    id: Optional[int] = None
    age: int
    address: Optional[str] = None

class Update(BaseModel):
    age: int

students = {}
@app.post("/student/")
async def create(student: Student):
    if student.id is not None:
        students[student.id] = student.dict()
        return {"student": students[student.id]}

@app.put("/student/{student_id}/age")
async def update_age(student_id: int, age_update: Update):
    if student_id in students:
        students[student_id]['age'] = age_update.age
        return {"student": students[student_id]}

@app.get("/student/{student_id}")
async def get(student_id: int):
    if student_id in students:
        return students[student_id]