from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from app.api.dependencies.opendota import opendota_profile_from_steam32id
from app.core.config import database_name, users_collection_name
from app.models.domain.users.User import UserInDB
from app.services.user import create_empty_user_from_open_dota_profile


async def get_user_by_steam32id(conn: AsyncIOMotorClient, steam32id: int) -> UserInDB:
    row = await conn[database_name][users_collection_name].find_one({"account_id": steam32id})
    if row:
        return UserInDB(**row)
    else:
        open_dota_profile = await opendota_profile_from_steam32id(steam32id)
        user = await create_user_from_open_dota_profile(conn, open_dota_profile)
        return user


async def create_user_from_open_dota_profile(
        conn: AsyncIOMotorClient,
        user: UserInDB = Depends(create_empty_user_from_open_dota_profile)
):
    await conn[database_name][users_collection_name].insert_one(user.dict())
    return user
