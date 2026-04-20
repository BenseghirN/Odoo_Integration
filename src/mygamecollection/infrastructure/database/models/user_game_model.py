from sqlalchemy import Column, Table, ForeignKey

from mygamecollection.infrastructure.database.base import Base

user_games_table = Table(
    "user_games",
    Base.metadata,
    Column("game_id", ForeignKey("games.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)