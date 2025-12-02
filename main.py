from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    name : str
    email: str
    institute: str
    adm: bool

banco : list[User] = []

app = FastAPI()

@app.get('/')
def read():
    return banco

@app.post('/')
def create(user : User):
    for a in banco:
        if a.email == user.email:
            return {'mensage' : 'Error Email already in use'}
    banco.append(user)
    return {'mensage' : 'Created with sucess'}

@app.delete('/')
def delete(user : User):
    for a in banco:
        if a == user:
            banco.remove(a)
            return {'mensage' : 'Deleted with sucess'}
    return {'mensage' : 'Error User doesnt exist'}

@app.get('/login')
def login(user : User):
    for a in banco:
        if a == user:
            return True
    return False