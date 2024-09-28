from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database for software courses
courses_db = []


# Pydantic model to represent a software course
class Course(BaseModel):
    id: int
    name: str
    description: str
    price: float
    duration: str  # e.g., "4 weeks", "6 months"


# 1. POST /courses: Create a new software course
@app.post("/courses", response_model=Course)
def create_course(course: Course):
    # Check if the course ID already exists
    for c in courses_db:
        if c["id"] == course.id:
            raise HTTPException(status_code=400, detail="Course ID already exists")

    courses_db.append(course.dict())
    return course


# 2. GET /courses: Retrieve the list of courses
@app.get("/courses", response_model=List[Course])
def get_courses():
    return courses_db
