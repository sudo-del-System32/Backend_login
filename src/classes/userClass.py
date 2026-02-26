from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    user_id: int
    user_name: str
    user_email: str
    password: str
    card_id: int

