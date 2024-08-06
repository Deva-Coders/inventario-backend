from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine("postgresql+asyncpg://postgres:iiiiiooooo@zaiko-db/postgres")
from models.create_all  import Base
# Create an asynchronous session
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


#connection = psycopg2.connect(host='zaiko-db', user='postgres', password='iiiiiooooo', dbname='postgres')

async def create_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        return  "Tables created successfully"
    except Exception as e:
        return str(e)

