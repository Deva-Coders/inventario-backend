from fastapi import APIRouter, HTTPException, Form, Request
from fastapi.responses import JSONResponse

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

from datetime import timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from schemas.user_schema import UserSchema, UserLogin
from typing import List
import logging
import services.user_service as us 
from services.token_service import login_for_access_token, verify_token

router = APIRouter( prefix="/user", tags=["user"])
logger = logging.getLogger()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")
valid_token = verify_token(Depends(oauth2_scheme))

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)

@router.post("/login")
async def post_login(u: UserLogin): 
    resp = await login_for_access_token(u.email, u.password) 
    if  resp.get("error"):
        logger.error(resp)
        return JSONResponse(content=resp, status_code=401)
    return JSONResponse(status_code= 200, content= resp)


@router.post("/add")
async def post_user(u: UserSchema, valid=Depends(get_current_user)):   
    logger.info(f"valid: {valid}")
    resp = await us.add_user(u)
    if  isinstance(resp,str):
        logger.error(resp)
        return JSONResponse(content=resp, status_code=500)
    return JSONResponse(status_code= 200, content= "User added successfully")


@router.get("/checkauth")
async def check_auth(auth:bool=True ):
    if  auth:
        return JSONResponse(status_code= 200, content= "Token is valid")
    return JSONResponse(status_code= 401, content= "Token is invalid")

@router.get("/list")
async def get_users():
    _users = await us.list_users()
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
    _users = await us.delete_user(id)
    if  isinstance(_users,str):
        logger.error(_users)
        return JSONResponse(content= _users , status_code=500)

    return JSONResponse (status_code= 200, content= "User deleted successfully")

    
@router.get("/password/recovery" )
async def login_password_recovery(email: str):
    resp = await us.password_recovery(email)
    if  resp.get("error"):
        logger.error(resp)
        return JSONResponse(content= "Wrong check Email" , status_code=500)

    return JSONResponse (status_code= 200, content= resp)


@router.put("/password/reset" )
async def login_password_reset(new_password: str, email: str): 
    resp = await us.password_reset(new_password, email)
    if  resp.get("error"):
        logger.error(resp)
        return JSONResponse(content= "Wrong check Email" , status_code=500)

    return JSONResponse (status_code= 200, content= resp)


@router.get("/security/question" )
async def security_question(email: str):
    resp = await us.security_question(email)
    if  resp.get("error"):
        logger.error(resp)
        return JSONResponse(content= resp.get("error") , status_code=500)

    return JSONResponse (status_code= 200, content= resp)
