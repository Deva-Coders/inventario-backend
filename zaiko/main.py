from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from db  import async_session as session
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


@app.get("/testdb")
async def test_db():
    try:
        async with session() as s:
            result = s.execute("SELECT 1")
            return {"status": "ok async"}
    except Exception as e:
        return {"status": "error", "error": str(e)}    






if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
