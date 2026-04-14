import os
import httpx

from mygamecollection.infrastructure.external.igdb.twitch_auth_client import TwitchAuthClient


class IgdbClient:
    def __init__(self, auth_client: TwitchAuthClient):
        self.auth_client = auth_client
        self.client_id = os.getenv('TWITCH_IGDB_CLIENT_ID')
        self.base_url = os.getenv('IGDB_BASE_URL')

    async def search_games(self, query: str):
        if not self.client_id:
            raise ValueError('Client ID not provided')
        if not self.base_url:
            raise ValueError('Base URL not provided')

        token = await self.auth_client.get_access_token()
        if not token:
            raise ValueError('Token not retrieved')

        body = f"""
            fields name,summary,first_release_date,cover.url;
            search "{query}";
            limit 10;
        """

        async with httpx.AsyncClient(
                headers={"Client-ID": self.client_id, "Authorization": f"Bearer {token}"}
        ) as client:
            response = await client.post(
                f"{self.base_url}/games",
                content=body.strip()
            )

            response.raise_for_status()
            return response.json()