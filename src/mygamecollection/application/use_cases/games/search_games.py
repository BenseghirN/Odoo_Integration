from mygamecollection.application.dtos.games.game_search_result_dto import SearchGamesResultDto
from mygamecollection.infrastructure.external.igdb.igdb_client import IgdbClient


class SearchGamesUseCase:
    def __init__(self, igdb_client: IgdbClient) -> None:
        self.igdb_client = igdb_client

    async def execute(self, query: str):
        results = await self.igdb_client.search_games(query)

        return [
            SearchGamesResultDto(
                igdb_id=game.get("id"),
                name=game.get("name"),
                summary=game.get("summary"),
                cover_url=game.get("cover", {}).get("url") if game.get("cover") else None,
                release_date=game.get("first_release_date"),
            )
            for game in results
        ]