from typing import List

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, Text, DateTime, UniqueConstraint
from datetime import datetime, timezone

from mygamecollection.infrastructure.database.base import Base
from mygamecollection.domain.entities.game import Game
from mygamecollection.infrastructure.database.models import UserModel
from mygamecollection.infrastructure.database.models.user_game_model import user_games_table


class GameModel(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    igdb_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    summary: Mapped[str | None] = mapped_column(Text)
    release_date : Mapped[str | None] = mapped_column(String)
    cover_url: Mapped[str | None] = mapped_column(String)
    # genres = Column(String)
    # platforms  Column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    users: Mapped[List[UserModel]] = relationship(secondary=user_games_table, back_populates="games")

    def to_domain(self) -> Game:
        return Game(
            igdb_id = self.igdb_id,
            name = self.name,
            summary = self.summary,
            release_date = self.release_date,
            cover_url = self.cover_url,
            id = self.id
        )

    @classmethod
    def from_domain(cls, game: Game):
        return cls(
            igdb_id = game.igdb_id,
            name = game.name,
            summary = game.summary,
            release_date = game.release_date,
            cover_url = game.cover_url,
        )
