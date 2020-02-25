from fastapi import APIRouter, Depends

from app.services.opendota import OpenDota

router = APIRouter()
api_key = "B58749D3D907C044D06A7EAB8CCDAE05"


@router.get('/profile/{steam32id}', name='opendota:profile')
async def get_profile(steam32id: int, open_dota: OpenDota = Depends(OpenDota)):
    return open_dota.get_player_infos(steam32id, api_key)