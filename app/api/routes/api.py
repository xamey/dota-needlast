from fastapi import APIRouter

from app.api.routes.endpoints import opendota, user, steam

router = APIRouter()
router.include_router(steam.router, tags=['steam'], prefix='/steam')
router.include_router(opendota.router, tags=['opendota'], prefix='/opendota')
router.include_router(user.router, tags=['user'], prefix='/user')
