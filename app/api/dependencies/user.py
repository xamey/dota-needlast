from fastapi import HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.status import HTTP_404_NOT_FOUND

from app.api.db.mongodb import get_database
from app.crud.user import get_user_by_steam32id


async def user_from_steam32id(
        steam32id: int,
        db: AsyncIOMotorClient = Depends(get_database)
):
    dbuser = await get_user_by_steam32id(db, steam32id)
    if not dbuser:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    return dbuser
