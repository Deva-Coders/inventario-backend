from models.models import User
from db  import async_session as session
from sqlalchemy.future import select
from sqlalchemy import update, delete
from schemas.user_schema import UserSchema, UserLogin, UserLoginReset
from decouple import config
from jose import JWTError, jwt
from datetime import datetime, timedelta
from pydantic import BaseModel

from passlib import hash



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
                logged = await mysession.execute(select(User).where(User.email == username and User.password == encrypted_password))
                return logged.scalar_one_or_none()

    except Exception as e:
        return  str(e)

async def login_reset_user(u: UserLoginReset):
    """Delete a user from the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                logged = await mysession.execute(selete(User).where(User.email == u.email and User.password == u.password))

                return logged.scalar_one_or_none()

    except Exception as e:
        return  str(e)

