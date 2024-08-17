from fastapi import APIRouter, HTTPException
from services.user_service import list_users, add_user, delete_user
from schemas.user_schema import UserSchema
from typing import List
import logging

router = APIRouter( prefix="/user", tags=["user"])
logger = logging.getLogger()

@router.post("/add")
async def post_user(u: List[UserSchema]):
    count_error = 0
    for x in u:
        resp = await add_user(x)
        if  isinstance(resp,str):
            logger.error(resp)
            count_error += 1
    #raise HTTPException(status_code=404, detail="User not added")

    return { "added": f"{len(u) - count_error}", "err": count_error}

@router.get("/list")
async def get_users():
    _users = await list_users()
    if  isinstance(_users,str):
        logger.error(_users)
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return [{"name": i.name} for i in _users]


@router.delete("/delete")
async def del_user(id: int):
    err = ""
    _users = await delete_user(id)
    if  isinstance(_users,str):
        logger.error(_users)
        err = _users
    return {"isok": True, "err": err}
