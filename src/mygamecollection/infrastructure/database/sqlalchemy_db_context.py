from sqlalchemy.ext.asyncio import AsyncSession
from mygamecollection.application.interfaces.db_context import IGameCollectionDbContext


class SQLAlchemyGameCollectionDbContext(IGameCollectionDbContext):
    def __init__(self, session: AsyncSession):
        self._session = session

    def add(self, obj) -> None:
        self._session.add(obj)

    async def commit(self) -> None:
        await self._session.commit()

    async def refresh(self, obj) -> None:
        await self._session.refresh(obj)

    async def execute(self, statement):
        return await self._session.execute(statement)

    def delete(self, obj) -> None:
        self._session.delete(obj)

    async def rollback(self) -> None:
        await self._session.rollback()

    async def close(self) -> None:
        await self._session.close()