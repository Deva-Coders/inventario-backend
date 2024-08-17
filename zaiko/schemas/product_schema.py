from pydantic import BaseModel


class ProductSchema(BaseModel):
    code: str
    name: str
    description: str
    unitPrice: int
    image: str
    supplier: int 
    category: int
    warehouse: int
