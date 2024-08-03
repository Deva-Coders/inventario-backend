from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine("postgresql+asyncpg://postgres:iiiiiooooo@zaiko-db/postgres")

# Create an asynchronous session
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


#connection = psycopg2.connect(host='zaiko-db', user='postgres', password='iiiiiooooo', dbname='postgres')

