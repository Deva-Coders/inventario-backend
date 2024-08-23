from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from services.product_service import list_products, add_product, delete_product, update_product
from schemas.product_schema import ProductSchema
from typing import List
import logging
import os

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

@router.put("/update")
async def put_product(id: int, p: ProductSchema):
    _products = await update_product(id, p)
    if  isinstance(_products,str):
        logger.error(_products)
        return JSONResponse(content= _products , status_code=500)

    return JSONResponse (status_code= 200, content= _products)

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        try:
            save_path = f"uploads/{file.filename}"
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "wb") as buffer:
                buffer.write(await file.read())
        except Exception as e:
            return JSONResponse (status_code= 500, content= {"msg":"Error uploading", "error": str(e)})

        return JSONResponse (status_code= 200, content={"filename": file.filename})
