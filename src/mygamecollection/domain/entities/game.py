from dataclasses import dataclass, field

from mygamecollection.domain.entities.user import User


@dataclass
class Game:
    igdb_id: int
    name: str
    summary: str | None = None
    release_date: str | None = None
    cover_url: str | None = None
    id: int | None = None
    users: list[User] = field(default_factory=list)

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Game name cannot be empty")

    @classmethod
    def create(
            cls,
            igdb_id: int,
            name: str,
            summary: str | None = None,
            release_date: str | None = None,
            cover_url: str | None = None
    ):
        if not name.strip():
            raise ValueError("Game name cannot be empty")

        return cls(
            igdb_id = igdb_id,
            name = name,
            summary = summary,
            release_date = release_date,
            cover_url = cover_url)

    def update(
            self,
            name: str,
            summary: str | None = None,
            release_date: str | None = None,
            cover_url: str | None = None
    ):
        if not name.strip():
            raise ValueError("Game name cannot be empty")

        self.name = name
        self.summary = summary
        self.release_date = release_date
        self.cover_url = cover_url