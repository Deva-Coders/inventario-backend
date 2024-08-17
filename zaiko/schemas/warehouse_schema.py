from pydantic import BaseModel


class WarehouseSchema(BaseModel):
    name: str
    location: str
