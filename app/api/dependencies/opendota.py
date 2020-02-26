from fastapi import Depends

from app.core.config import STEAM_API_KEY
from app.models.domain.open_dota_profile.OpenDotaProfile import OpenDotaProfile
from app.services.opendota import OpenDota


async def opendota_profile_from_steam32id(
        steam32id: int,
        open_dota: OpenDota = Depends(OpenDota)
) -> OpenDotaProfile:
    return open_dota.get_player_infos_from_steam32id(steam32id, STEAM_API_KEY)
