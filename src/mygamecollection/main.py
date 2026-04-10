from mygamecollection.application.interfaces.db_context import IGameCollectionDbContext
from mygamecollection.application.use_cases.games.get_all_games import GetAllGamesAsync
from mygamecollection.infrastructure.database.session import SessionLocal
from mygamecollection.infrastructure.database.sqlalchemy_db_context import SQLAlchemyGameCollectionDbContext
import asyncio

async def main():
    async with SessionLocal() as session:
        db_context: IGameCollectionDbContext = SQLAlchemyGameCollectionDbContext(session)
        try:
            print(f"DbContext initialized: {db_context}")
            use_case = GetAllGamesAsync(db_context)
            games = await use_case.execute()

            print(f"{len(games)} game(s) found")
            for game in games:
                print(f"{game.id} - {game.name}")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await db_context.close()

if __name__ == "__main__":
    asyncio.run(main())