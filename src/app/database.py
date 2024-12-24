from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .core import settings

engine = create_async_engine(
    url=f"{settings.DATABASE_URL}/test-db",
    echo=True,
    pool_size=10,
    max_overflow=20,
)

# Async session for async queries
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session
