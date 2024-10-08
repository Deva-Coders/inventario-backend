from models.models import Product
from db  import async_session as session
from sqlalchemy.future import select
from sqlalchemy import update, delete
from schemas.product_schema import ProductSchema

async def list_products():
    # List all products
    try:
        async with session() as mysession:
            async with mysession.begin():
                data = await mysession.execute(select(Product))
                return data.scalars().all()

    except Exception as e:
        return  str(e)


async def add_product(product: ProductSchema):
    """Add a product to the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                new_product = Product(code=product.code, name=product.name,description=product.description, unitPrice=product.unitPrice, image=product.image, supplier=product.supplier, category=product.category, ware=product.warehouse)
                mysession.add(new_product)
                await mysession.commit()        

    except Exception as e:
        return  str(e)

async def delete_product(id: int):
    """Delete a product from the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                await mysession.execute(delete(Product).where(Product.id == id))
                await mysession.commit()

    except Exception as e:
        return  str(e)


async def update_product(id: int, p: ProductSchema):
    """Update a product from the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                result=await mysession.execute(update(Product).where(Product.id == id).values(
                name =p.name,
                code =  p.code,
                description = p.description,
                unitPrice=p.unitPrice, 
                image = p.image, 
                supplier=p.supplier,
                category=p.category,
                ware=p.warehouse
                ))
                if result.rowcount == 1:
                    await mysession.commit()
                    return True
                return False

    except Exception as e:
        return  str(e)
