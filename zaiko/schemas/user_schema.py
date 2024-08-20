from pydantic import BaseModel


class UserSchema(BaseModel):
    fullName: str
    email: str
    phone: str
    secretAnswer: str
    secretQuestion: str
    password: str
    role: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserLoginReset(BaseModel):
    email: str
    old_password: str
    new_password: str

