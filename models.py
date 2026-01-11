from pydantic import BaseModel


# class User:
#     id:int
#     name:str
#     salary:float
#     email:str

class User(BaseModel):
    id:int
    name:str
    salary:float
    email:str

    # def __init__(self, id:int, name:str, salary:float, email:str):
    #     self.id = id
    #     self.name = name
    #     self.salary = salary
    #     self.email = email