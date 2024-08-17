from models.models import Category
from db  import async_session as session
from sqlalchemy.future import select
from sqlalchemy import update, delete
from schemas.category_schema import CategorySchema

async def list_categorys():
    # List all categorys
    try:
        async with session() as mysession:
            async with mysession.begin():
                data = await mysession.execute(select(Category))
                return data.scalars().all()

    except Exception as e:
        return  str(e)


async def add_category(category: CategorySchema):
    """Add a category to the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                new_category = Category(name=category.name)
                mysession.add(new_category)
                await mysession.commit()        

    except Exception as e:
        return  str(e)

async def delete_category(id: int):
    """Delete a category from the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                await mysession.execute(delete(Category).where(Category.id == id))
                await mysession.commit()

    except Exception as e:
        return  str(e)
