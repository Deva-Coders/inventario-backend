from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.user_service import list_users, add_user, delete_user
from schemas.user_schema import UserSchema
from typing import List
import logging

router = APIRouter( prefix="/user", tags=["user"])
logger = logging.getLogger()

@router.post("/add")
async def post_user(u: UserSchema):
    resp = await add_user(u)
    if  isinstance(resp,str):
        logger.error(resp)
        return JSONResponse(content=resp, status_code=500)
    return JSONResponse(status_code= 200, content= "User added successfully")


@router.get("/list")
async def get_users():
    _users = await list_users()
    if  isinstance(_users,str):
        logger.error(_users)
        return JSONResponse(content=_users, status_code=500)
    else:
        return  JSONResponse(content=[{"id": i.id,
                                       "fullName": i.fullName,
                                       "email": i.email,
                                       "role": i.role,
                                       "phone": i.phone,
                                       "password": i.password,
                                       "secretQuestion": i.secretQuestion,
                                       "secretAnswer": i.secretAnswer
                                       } for i in _users]
                        , status_code=200
                        )


@router.delete("/delete")
async def del_user(id: int):
    _users = await delete_user(id)
    if  isinstance(_users,str):
        logger.error(_users)
        return JSONResponse(content= _users , status_code=500)

    return JSONResponse (status_code= 200, content= "User deleted successfully")
