from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: str
    email: str
    password: str
    role: str

class UserLogin(User):
    email: str
    password: str

