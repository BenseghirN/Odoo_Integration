from typing import List

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, DateTime
from datetime import datetime, timezone

from mygamecollection.infrastructure.database.base import Base
from mygamecollection.infrastructure.database.models import GameModel
from mygamecollection.infrastructure.database.models.user_game_model import user_games_table
from mygamecollection.domain.entities.user import User


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    login: Mapped[str] = mapped_column(String(50), nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    users: Mapped[List[GameModel]] = relationship(secondary=user_games_table, back_populates="users")

    def to_domain(self) -> User:
        return User(
            login= self.login,
            first_name = self.first_name,
            last_name = self.last_name,
            id=self.id
        )

    @classmethod
    def from_domain(cls, user: User):
        return cls(
            login= user.login,
            first_name = user.first_name,
            last_name = user.last_name
        )
