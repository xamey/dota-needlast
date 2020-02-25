from fastapi import APIRouter

from app.api.routes import steam, opendota

router = APIRouter()
router.include_router(steam.router, tags=['steam'], prefix='/steam')
router.include_router(opendota.router, tags=['opendota'], prefix='/opendota')