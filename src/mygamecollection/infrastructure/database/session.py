import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable not found")

engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(engine, autocommit=False, autoflush=False, expire_on_commit=False)