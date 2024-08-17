from fastapi import APIRouter, HTTPException
from services.supplier_service import list_suppliers, add_supplier, delete_supplier
from schemas.supplier_schema import SupplierSchema
from typing import List
import logging

router = APIRouter( prefix="/supplier", tags=["supplier"])
logger = logging.getLogger()

@router.post("/add")
async def post_supplier(param: SupplierSchema):
    resp = await add_supplier(param)
    if  isinstance(resp,str):
        logger.error(resp)
        raise HTTPException(status_code=500, content=resp)

    return { "status_code": 200, "content": "suppliers added"}

@router.get("/list")
async def get_suppliers():
    _suppliers = await list_suppliers()
    if  isinstance(_suppliers,str):
        logger.error(_suppliers)
        raise HTTPException(status_code=500, content= _suppliers)
    else:
        return {"status_code": 200,
                "content": [{"id": i.id, "name": i.name} 
                for i in _suppliers]
                }


@router.delete("/delete")
async def del_supplier(id: int):
    _suppliers = await delete_supplier(id)
    if  isinstance(_suppliers,str):
        logger.error(_suppliers)
        raise HTTPException( status_code=500, content=_suppliers)
    return {"status_code": 200, "content":""}
