from fastapi import FastAPI, HTTPException
from models import User


app = FastAPI()

@app.get("/")
def welcome():
    return "Welcome to FastAPI Training"

# users =[
#     User(1, "Archana", 25816, "archtest@gmail.com"),
#     User(2, "Anita", 25816, "anitatest@gmail.com")
# ]

users =[
    User(id=1, name ="Archana", salary=25816, email="archtest@gmail.com"),
    User(id=2, name="Anita", salary=25816, email="anitatest@gmail.com"),
    User(id=4, name="Ajay", salary=35816, email="ajaytest@gmail.com")
]

@app.get("/users")
def get_users():
    return users

@app.get("/user/{id}")
def get_user_by_id(id:int):
    for user in users:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/user")
def create_user(user: User):
    users.append(user)
    return user

@app.put("/user")
def update_user(id:int, user: User):
    for u in range(len(users)):
        if users[u].id == id:
            users[u] = user
            return "user added successfully"
    return "User Not Found"

@app.delete("/user")
def delete_user(id:int):
    for u in range(len(users)):
        if users[u].id == id:
            del users[u]
            return "user deleted successfully"
    return "User Not Found"





    


