import asyncio
from dotenv import load_dotenv

from mygamecollection.domain.entities.game import Game

load_dotenv()

from mygamecollection.infrastructure.database.session import SessionLocal
from mygamecollection.application.use_cases.games.search_games import SearchGamesUseCase
from mygamecollection.infrastructure.external.igdb.igdb_client import IgdbClient
from mygamecollection.infrastructure.external.igdb.twitch_auth_client import TwitchAuthClient



async def main():
    twitch_auth_client = TwitchAuthClient()
    igdb_client = IgdbClient(twitch_auth_client)
    search_games = SearchGamesUseCase(igdb_client)

    results = await search_games.execute(input("What game do you want to search?: "))

    for result in results:
        print(result.name)

if __name__ == "__main__":
    asyncio.run(main())