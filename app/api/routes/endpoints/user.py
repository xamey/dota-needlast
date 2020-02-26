from fastapi import APIRouter, Depends

from app.api.dependencies.user import user_from_steam32id
from app.models.domain.users.User import UserOut

router = APIRouter()


@router.get('/{steam32id}', response_model=UserOut)
async def user_from_steam32id(
        user=Depends(user_from_steam32id)
) -> UserOut:
    return user
