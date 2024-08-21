from models.models import User
from db  import async_session as session
from sqlalchemy.future import select
from sqlalchemy import update, delete
from schemas.user_schema import UserSchema, UserLogin, UserLoginReset
from decouple import config
from jose import JWTError, jwt
from datetime import datetime, timedelta
from pydantic import BaseModel

from passlib import hash,pwd



async def list_users():
    # List all users
    try:
        async with session() as mysession:
            async with mysession.begin():
                data = await mysession.execute(select(User))
                return data.scalars().all()

    except Exception as e:
        return  str(e)


async def add_user(user: UserSchema):
    """Add a user to the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                new_user = User(fullName=user.fullName, 
                    email=user.email, 
                    password=hash.bcrypt.encrypt(user.password),
                    phone=user.phone,
                    secretQuestion=user.secretQuestion,
                    secretAnswer=hash.bcrypt.encrypt(user.secretAnswer),
                    role= "user" if user.role !="admin" else "admin"
                    )
                mysession.add(new_user)
                await mysession.commit()        

    except Exception as e:
        return  str(e)

async def delete_user(id: int):
    """Delete a user from the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                await mysession.execute(delete(User).where(User.id == id))
                await mysession.commit()

    except Exception as e:
        return  str(e)

async def authenticate_user(username: str, password: str):
    """Look up a confirm exist user in  database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                encrypted_password = hash.bcrypt.encrypt(password)
                logged = await mysession.execute(select(User).where(User.email == username))
                user = logged.scalar_one_or_none()
                if user and hash.bcrypt.verify(password, user.password):
                    return user 
                return None

    except Exception as e:
        #return {"isValidAuth": False, "error": str(e)} 
        return None

async def password_reset(new_password:str, token: str):
    """Change password for user in database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                encrypted_password = hash.bcrypt.encrypt(new_password)
                result = await mysession.execute(update(User).where(User.email == token).values(password=encrypted_password))
                if result.rowcount == 1:
                    await mysession.commit()
                    return {"isReset": True}

        return {"isReset": False, "error": "User not found"} 

    except Exception as e:
        return {"isReset": False, "error": str(e)} 

async def password_recovery(email:str):
    """Recieve email and send password to email"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                logged = await mysession.execute(select(User).where(User.email == email))
                user = logged.scalar_one_or_none()

                recovery_password = pwd.genword(length=10)
                result = await password_reset(recovery_password, email)
                if result.get("isReset"):
                    return {"isSendedEmail": True, "email": email, "password": recovery_password}
                else:
                    return {"isSendedEmail": False, "error":  result.get("error")}

    except Exception as e:
        return  {"error": str(e)}

