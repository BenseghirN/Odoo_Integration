import os
import httpx


class TwitchAuthClient:
    def __init__(self):
        self.token_url = os.getenv('TWITCH_TOKEN_URL') or "https://id.twitch.tv/oauth2/token"
        self.client_id = os.getenv("TWITCH_IGDB_CLIENT_ID")
        self.client_secret = os.getenv("TWITCH_IDGB_CLIENT_SECRET")

    async def get_access_token(self) -> str:
        if not self.client_id:
            raise ValueError('Client ID not provided')
        if not self.client_secret:
            raise ValueError('Client secret not provided')
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.token_url,
                    params={
                        'client_id': self.client_id,
                        'client_secret': self.client_secret,
                        'grant_type': 'client_credentials'
                    }
                )

                response.raise_for_status()

                data = response.json()
                if "access_token" not in data:
                    raise Exception('Invalid response from Twitch API: no access_token provided')

                return data['access_token']
        except Exception as err:
            raise Exception("An error occurred while getting the access token", err)