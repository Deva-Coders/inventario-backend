from fastapi import APIRouter, HTTPException
from services.warehouse_service import list_warehouses, add_warehouse, delete_warehouse
from schemas.warehouse_schema import WarehouseSchema
from typing import List
import logging

router = APIRouter( prefix="/warehouse", tags=["warehouse"])
logger = logging.getLogger()

@router.post("/add")
async def post_warehouse(param: WarehouseSchema):
    resp = await add_warehouse(param)
    if  isinstance(resp,str):
        logger.error(resp)
        raise HTTPException(status_code=500, content=resp)

    return { "status_code": 200, "content": "warehouses added"}

@router.get("/list")
async def get_warehouses():
    _warehouses = await list_warehouses()
    if  isinstance(_warehouses,str):
        logger.error(_warehouses)
        raise HTTPException(status_code=500, content= _warehouses)
    else:
        return {"status_code": 200,
                "content": [{"id": i.id, "name": i.name, "location": i.location} 
                for i in _warehouses]
                }


@router.delete("/delete")
async def del_warehouse(id: int):
    _warehouses = await delete_warehouse(id)
    if  isinstance(_warehouses,str):
        logger.error(_warehouses)
        raise HTTPException( status_code=500, content=_warehouses)
    return {"status_code": 200, "content":""}
