from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from mygamecollection.domain.enums.game_status import GameStatus
if TYPE_CHECKING:
    from mygamecollection.infrastructure.database.models import UserModel, GameModel
from mygamecollection.infrastructure.database.base import Base

class UserGameModel(Base):
    __tablename__ = "user_games"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"), primary_key=True)
    status: Mapped[GameStatus] = mapped_column(SAEnum(GameStatus), nullable=False, default=GameStatus.TO_DO)

    user: Mapped[UserModel] = relationship(back_populates="game_entries")
    game: Mapped[GameModel] = relationship(back_populates="user_entries")