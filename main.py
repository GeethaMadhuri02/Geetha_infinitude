from fastapi import FastAPI
app = FastAPI()
employee={1:{"name":"Geetha","role":"Student"}}
#@app.get("/basic")
#def test():
#   return {"Test":"Manual input"}

@app.get("/test/{employee_id}")
def test(employee_id:int ):
    if employee_id in employee:
        return employee[employee_id]
    return {"Data":"Not found"}
