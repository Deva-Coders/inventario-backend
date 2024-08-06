from models.create_all import User
from db  import async_session as session
from sqlalchemy.future import select
from sqlalchemy import update, delete
from schemas.user_schema import UserSchema

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
                new_user = User(name=user.name, email=user.email, password=user.password)
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
