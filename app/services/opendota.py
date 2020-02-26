import requests

from app.models.domain.open_dota_profile.OpenDotaProfile import OpenDotaProfile


class OpenDota():
    _provider = "https://api.opendota.com/api/"

    def get_player_infos_from_steam32id(
            self,
            steam32id: int,
            api_key: str
    ) -> OpenDotaProfile:
        r = requests.get("{0}players/{1}?api_key={2}".format(self._provider, str(steam32id), api_key))
        return OpenDotaProfile(**r.json())
