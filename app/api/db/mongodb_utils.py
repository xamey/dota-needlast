import logging

from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db


async def connect_to_mongo():
    logging.info("Connecting to mongoDB...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    logging.info("Connected to mongoDB！")


async def close_mongo_connection():
    logging.info("Closing mongoDB connection...")
    db.client.close()
    logging.info("mongoDB connection closed！")