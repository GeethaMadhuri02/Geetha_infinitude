from fastapi import FastAPI

user_db={
    'charan': {'username':'charan','date joined':'23-07-2024','location':'Hyderabad'},
    'krishna':{'username':'krishna','date joined':'23-07-2024','location':'Banglore'}
}
app=FastAPI()
@app.get('/users')
def get_users():
    user_list=list(user_db.values())
    return user_list

@app.put('/users/{username}')
def put_users_path(username:str):
    return user_db[username]