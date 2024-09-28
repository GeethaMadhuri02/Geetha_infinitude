from fastapi import FastAPI, BackgroundTasks, Path
from pydantic import BaseModel
import asyncio

app = FastAPI()

class Employee(BaseModel):
    name:str
    role:str
employee = {
    1:{
        "name": "Ganesh",
        "role": "Tester"
    }
}

async def task_a():
    await asyncio.sleep(2)
    print("Task A completed.")

async def task_b():
    await asyncio.sleep(3)
    print("Task B completed.")

@app.get("/run-tasks")
async def run_tasks(bg_task: BackgroundTasks):
    bg_task.add_task(task_a)
    bg_task.add_task(task_b)
    return {"message": "Tasks scheduled"}

# @app.get("/test/{employe_id}")
# def test(employe_id:int =  Path(description = "ID is required", gt=0 , le=3)):
#     if employe_id in employee:
#         return employee[employe_id]
#     return {"Data":"Not found"}


@app.get("/")
def read_root():
    return {"Hello": "World"}