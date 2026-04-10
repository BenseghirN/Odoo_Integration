from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Text, DateTime
from datetime import datetime, timezone

from mygamecollection.infrastructure.database.base import Base
from mygamecollection.domain.entities.game import Game

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

    def to_domain(self) -> Game:
        return Game(
            igdb_id = self.igdb_id,
            name = self.name,
            summary = self.summary,
            release_date = self.release_date,
            cover_url = self.cover_url,
            id = self.id
        )

    @staticmethod
    def from_domain(game: Game):
        return GameModel(
            igdb_id = game.igdb_id,
            name = game.name,
            summary = game.summary,
            release_date = game.release_date,
            cover_url = game.cover_url,
        )
