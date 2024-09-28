from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class One(BaseModel):
    title : str
    body :str
    pageno: int

# @app.get("/blog/unpublished")
# def unpublished():
#     return {"data":"all are unpublished"}
#
@app.get("/blog/{id}")
def show(id:int):
    return {'data':id}

@app.put("/add")
async def add(item:One):
    return item


@app.post("/post")
async def update(we2:One):
    return we2

@app.delete("/del")
async def delete():
    return {"role":"Develooper"}

@app.patch("/patch")
async def patch():
    return {"role":"Develooper"}


# @app.get("/get")
# def read():
#     return {"name":"Laxmi"}
# @app.get("/blog/{id}")
# def show(id):
#     return {"data":id}

# @app.post("/post")
# async def update():
#     return {"role ": " Develooper"}
#
# @app.put("/put/username")
# async def add():
#     return{"age":"22"}