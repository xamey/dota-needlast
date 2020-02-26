from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.db.mongodb_utils import connect_to_mongo, close_mongo_connection
from app.api.routes.api import router as api_router
from app.core.config import API_PREFIX

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(api_router, prefix=API_PREFIX)
