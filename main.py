from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    name : str
    email: str
    institute: str
    adm: Optional[bool] = False

banco : List[User] = []

app = FastAPI()


@app.get('/')
def read():
    return banco


@app.post('/')
def create(userQuerry : User):
    for user in banco:
        if user.email == userQuerry.email:
            return {'mensage' : 'Error Email already in use'}
    banco.append(userQuerry)
    return {'mensage' : 'Created with sucess'}


@app.delete('/')
def delete(email : Optional[str] = None):
    for user in banco:
        if user.email == email:
            banco.remove(user)
            return {'mensage' : 'Deleted with sucess'}
    return {'mensage' : 'Error User doesnt exist'}


@app.get('/login')
def login(userQuerry : User):
    for user in banco:
        if user == userQuerry:
            return True
    return False