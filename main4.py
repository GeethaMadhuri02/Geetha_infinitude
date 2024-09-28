from fastapi import FastAPI
from fastapi import FastAPI,Path
from pydantic import BaseModel

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


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
# @app.get("/basic")
# def test():
#     return {"Test":"Manual input"}

@app.get("/test/{employe_id}")
def test(employe_id:int =  Path(description = "ID is required", gt=0 , le=3)):
    if employe_id in employee:
        return employee[employe_id]
    return {"Data":"Not found"}

