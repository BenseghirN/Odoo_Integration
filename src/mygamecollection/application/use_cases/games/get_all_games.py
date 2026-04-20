from sqlalchemy import select

from mygamecollection.application.interfaces.db_context import IGameCollectionDbContext
from mygamecollection.domain.entities.game import Game
from mygamecollection.infrastructure.database.models.game_model import GameModel


class GetAllGamesAsync:
    def __init__(self, db_context: IGameCollectionDbContext):
        self._db_context = db_context

    async def execute(self) -> list[Game]:
        result = await self._db_context.execute(
            select(GameModel).order_by(GameModel.name.asc())
        )
        return [model.to_domain() for model in result.scalars().all()]