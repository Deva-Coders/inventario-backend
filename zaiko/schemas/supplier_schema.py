from pydantic import BaseModel


class SupplierSchema(BaseModel):
    name: str
    address: str
    phone: str 
    email: str

