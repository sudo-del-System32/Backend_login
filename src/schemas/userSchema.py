from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    user_id: int = None
    name: str = None
    birthday: int = None

    user_name: str = None
    email: str = None
    password: str = None


