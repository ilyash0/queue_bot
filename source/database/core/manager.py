from typing import Any

from loguru import logger
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from source.config import settings


class DatabaseManager:
    def __init__(self, db_url: str, **kwargs: Any):
        self.engine: AsyncEngine = create_async_engine(
            db_url,
            **kwargs,
        )
        self.session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )

    async def dispose(self):
        await self.engine.dispose()
        logger.info("Database connection closed")


db_manager = DatabaseManager(
    settings.db.postgres_connection(),
)
