import requests
import os

twitch_client_id = os.environ.get("TWITCH_CLIENT_ID")
twitch_client_secret = os.environ.get("TWITCH_CLIENT_SECRET")
twitch_token = os.environ.get("TWITCH_TOKEN")
TWITCH_USERS_ENDPOINT = "https://api.twitch.tv/helix/users"

twitch_header = {
    "Authorization": f"Bearer {twitch_client_secret}",
    "Client-Id": twitch_client_id,
}

twitch_parameters = {
    "login": "timtam89" 
}
response = requests.get(url=TWITCH_USERS_ENDPOINT, params=twitch_parameters, headers=twitch_header)
response.raise_for_status()
data = response.json()
print(data)