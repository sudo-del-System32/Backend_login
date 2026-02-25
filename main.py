from fastapi import FastAPI
from src.controllers import userControllers

app = FastAPI()

@app.get('/')
def root():
    return {'mensagem' : 'BEM VINDO!'}




app.include_router(userControllers.router)