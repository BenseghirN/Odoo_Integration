from __future__ import annotations
from typing import List, TYPE_CHECKING

from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from mygamecollection.infrastructure.database.base import Base
if TYPE_CHECKING:
    from mygamecollection.infrastructure.database.models import GameModel

game_genre_table: Table = Table(
    "game_genres",
    Base.metadata,
    Column("game_id", ForeignKey("games.id"), primary_key=True),
    Column("genre_id", ForeignKey("genres.id"), primary_key=True),
)

class GenreModel(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    igdb_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    games: Mapped[List[GameModel]] = relationship(secondary=game_genre_table, back_populates="genres")

