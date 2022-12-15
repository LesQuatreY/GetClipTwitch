import requests
import json

from utils import (get_token)

class GetClip:

    MY_TOKEN = get_token()
    CLIENT_ID = "fmxbop0687cv14jk7j1egwrb9p7rml"

    def __init__(self):
        pass

    def _request(self, url, params=""):
        import urllib.parse
        return requests.get(url+urllib.parse.urlencode(params), headers={
                'Authorization': f'Bearer {GetClip.MY_TOKEN}',
                'Client-Id': GetClip.CLIENT_ID
                }
            )

    def _get_id_streamer(self,name_streamer):
        return json.loads(
            self._request(
            f"https://api.twitch.tv/helix/users?login={name_streamer}"
            ).text
        )['data'][0]['id']

    def url_best_clip_streamer(self,name_streamer,params,top=1):
        et="&" if params else "" 
        return json.loads(self._request(
                f"https://api.twitch.tv/helix/clips?broadcaster_id={self._get_id_streamer(name_streamer)}{et}",
                params=params
            ).text)['data'][:top]#.get("url")

    def _get_id_game(self, name_game):
        return json.loads(
            self._request(
            f"https://api.twitch.tv/helix/games?name={name_game}"
            ).text
            )['data'][0]['id']

    def url_best_clip_game(self,name_game,params,top=1):
        et="&" if params else ""  
        return json.loads(
            self._request(
                f"https://api.twitch.tv/helix/clips?game_id={self._get_id_game(name_game)}{et}",
                params=params
            ).text
        )['data'][:top]#.get("url")
