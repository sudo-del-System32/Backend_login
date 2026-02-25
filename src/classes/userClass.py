from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    nome: str
    idade: int

    nomeDeUsuario: str
    email: str
    senha: str
    
    admin : bool
    createdBy: str


