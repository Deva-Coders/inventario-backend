from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
def read_root():
    return {"iniciado": "Zaiko Inventory API"}







if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
