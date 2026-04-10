from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime, timezone
from .base import Base

class GameModel(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    igdb_id = Column(Integer, unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    summary = Column(Text) 
    release_date = Column(String)
    cover_url = Column(String)
    # genres = Column(String)
    # platforms  Column(String)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))