from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.category_service import list_categorys, add_category, delete_category
from schemas.category_schema import CategorySchema
from typing import List
import logging

router = APIRouter( prefix="/category", tags=["category"])
logger = logging.getLogger()

@router.post("/add")
async def post_category(param: CategorySchema):
    resp = await add_category(param)
    if  isinstance(resp,str):
        logger.error(resp)
        return JSONResponse(content=resp, status_code=500)

    return JSONResponse(status_code=200, content="category added")

@router.get("/list")
async def get_categorys():
    _categorys = await list_categorys()
    if  isinstance(_categorys,str):
        logger.error(_categorys)
        raise HTTPException(status_code=500, content="Category not found")
    else:
        return {"status_code": 200, "content": [{"name": i.name} for i in _categorys]}
        

@router.delete("/delete")
async def del_category(id: int):
    _categorys = await delete_category(id)
    if  isinstance(_categorys,str):
        logger.error(_categorys)
        #return { "status_code": 500, "content": _categorys}
        raise HTTPException(status_code=500, content=_categorys)
    return { "status_code": 200, "content": "category added"}
