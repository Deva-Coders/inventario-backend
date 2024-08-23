from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from decouple import config
dbuser = config('DB_USER')  
dbpassword = config('DB_PASSWORD')
engine = create_async_engine(f"postgresql+asyncpg://{dbuser}:{dbpassword}@zaiko-db/postgres")
from models.models  import Base
# Create an asynchronous session
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

async def create_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        return  "Tables created successfully"
    except Exception as e:
        return str(e)
