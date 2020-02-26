from fastapi import APIRouter, Depends

from app.api.dependencies.opendota import opendota_profile_from_steam32id
from app.models.domain.open_dota_profile.OpenDotaProfile import OpenDotaProfile
from app.models.schemas.OpenDotaProfileInResponse import OpenDotaProfileInResponse

router = APIRouter()


@router.get('/profile/{steam32id}', name='opendota:profile', response_model=OpenDotaProfileInResponse)
async def profile_from_steam32id(
        open_dota_profile: OpenDotaProfile = Depends(opendota_profile_from_steam32id)
) -> OpenDotaProfileInResponse:
    return open_dota_profile
