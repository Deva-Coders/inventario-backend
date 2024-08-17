from models.models import Supplier
from db  import async_session as session
from sqlalchemy.future import select
from sqlalchemy import update, delete
from schemas.supplier_schema import SupplierSchema

async def list_suppliers():
    # List all suppliers
    try:
        async with session() as mysession:
            async with mysession.begin():
                data = await mysession.execute(select(Supplier))
                return data.scalars().all()

    except Exception as e:
        return  str(e)


async def add_supplier(supplier: SupplierSchema):
    """Add a supplier to the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                new_supplier = Supplier(name=supplier.name,
                                        email=supplier.email,
                                        address=supplier.address,
                                        phone=supplier.phone  
                                        )
                mysession.add(new_supplier)
                await mysession.commit()        

    except Exception as e:
        return  str(e)

async def delete_supplier(id: int):
    """Delete a supplier from the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                await mysession.execute(delete(Supplier).where(Supplier.id == id))
                await mysession.commit()

    except Exception as e:
        return  str(e)
