from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.product_service import list_products, add_product, delete_product
from schemas.product_schema import ProductSchema
from typing import List
import logging

router = APIRouter( prefix="/product", tags=["product"])
logger = logging.getLogger()

@router.post("/add")
async def post_product(param: ProductSchema):
    resp = await add_product(param)
    if  isinstance(resp,str):
        logger.error(resp)
        return JSONResponse(content=resp, status_code=500)
    return JSONResponse(status_code= 200, content= resp)

@router.get("/list")
async def get_products():
    _products = await list_products()
    if  isinstance(_products,str):
        logger.error(_products)
        return JSONResponse(content= _products , status_code=500)
    else:
        return JSONResponse(status_code= 200, 
                        content= [{"id": i.id,
                                "code": i.code,
                                "name": i.name, 
                                "unitPrice": i.unitPrice,
                                "category": i.category,
                                "supplier": i.category,
                                "warehouse": i.ware
                                } 
                                for i in _products]
                       )        

@router.delete("/delete")
async def del_product(id: int):
    _products = await delete_product(id)
    if  isinstance(_products,str):
        logger.error(_products)
        return JSONResponse(content= _products , status_code=500)

    return JSONResponse (status_code= 200, content= _products)
