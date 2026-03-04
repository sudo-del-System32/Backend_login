import os, uvicorn
from fastapi import FastAPI
from src.controllers import userControllers, cardControllers

app = FastAPI(title= "Api card social midia test")

@app.get('/')
async def root():
    return {'mensagem' : 'API TEST OK'}


# ---- ROUTERS ---- 
app.include_router(userControllers.router)
app.include_router(cardControllers.router)


# ---- MAIN ----
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)


