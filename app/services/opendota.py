import requests

class OpenDota():
    _provider = "https://api.opendota.com/api/"

    def get_player_infos(self, steam32id: int, api_key: str):
        r = requests.get(self._provider+"players/"+str(steam32id)+"?api_key="+api_key)
        return r.json()