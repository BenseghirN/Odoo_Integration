import asyncio
from dotenv import load_dotenv
load_dotenv()

from mygamecollection.infrastructure.database.session import SessionLocal
from mygamecollection.application.use_cases.games.search_games import SearchGamesUseCase
from mygamecollection.infrastructure.external.igdb.igdb_client import IgdbClient
from mygamecollection.infrastructure.external.igdb.twitch_auth_client import TwitchAuthClient



async def main():
    twitch_auth_client = TwitchAuthClient()
    igdb_client = IgdbClient(twitch_auth_client)
    search_games = SearchGamesUseCase(igdb_client)

    results = await search_games.execute("God Of War")
    print(results)

if __name__ == "__main__":
    asyncio.run(main())