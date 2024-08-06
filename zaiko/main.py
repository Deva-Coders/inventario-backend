from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from db  import async_session as session, create_tables
from routes import user
import json
import uvicorn

app = FastAPI()
app.include_router(user.router)

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
def read_root():
    return {"iniciado": "Zaiko Inventory API"}


@app.get("/initdb")
async def init_db():
    s = await create_tables()
    return {"status": s}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
