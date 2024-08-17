from models.models import Warehouse
from db  import async_session as session
from sqlalchemy.future import select
from sqlalchemy import update, delete
from schemas.warehouse_schema import WarehouseSchema

async def list_warehouses():
    # List all warehouses
    try:
        async with session() as mysession:
            async with mysession.begin():
                data = await mysession.execute(select(Warehouse))
                return data.scalars().all()

    except Exception as e:
        return  str(e)


async def add_warehouse(warehouse: WarehouseSchema):
    """Add a warehouse to the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                new_warehouse = Warehouse(name=warehouse.name, location=warehouse.location)
                mysession.add(new_warehouse)
                await mysession.commit()        

    except Exception as e:
        return  str(e)

async def delete_warehouse(id: int):
    """Delete a warehouse from the database"""
    try:
        async with session() as mysession:
            async with mysession.begin():
                await mysession.execute(delete(Warehouse).where(Warehouse.id == id))
                await mysession.commit()

    except Exception as e:
        return  str(e)
