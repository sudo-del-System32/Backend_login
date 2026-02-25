from pydantic import BaseModel
from datetime import datetime as dt

class User(BaseModel):
    user_id: int
    name: str
    birthday: dt

    user_name: str
    email: str
    password: str
    
    admin : bool
    created_by: str


