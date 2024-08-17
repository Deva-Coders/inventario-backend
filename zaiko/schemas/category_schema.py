from pydantic import BaseModel


class CategorySchema(BaseModel):
    name: str

class CategoryDel(BaseModel):
    id: int

class CategoryMod(BaseModel):
    id: int
    name: str
