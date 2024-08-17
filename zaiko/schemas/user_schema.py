from pydantic import BaseModel


class UserSchema(BaseModel):
    fullName: str
    email: str
    phone: str
    secretAnswer: str
    secretQuestion: str
    password: str
    role: str
