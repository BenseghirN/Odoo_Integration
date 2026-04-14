from dataclasses import dataclass


@dataclass
class SearchGamesResultDto:
    igdb_id: int
    name: str
    summary: str | None
    cover_url: str | None
    release_date: str | None