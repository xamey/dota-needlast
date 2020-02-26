from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.services.steam import SteamSignIn

router = APIRouter()
api_steam_url = "http://127.0.0.1:8000/api/steam"


@router.get('/login', name="steam:redirect-to-steam-login")
async def redirect_to_steam_login(steam_signin: SteamSignIn = Depends(SteamSignIn)) -> None:
    url = steam_signin.ConstructURL(api_steam_url + '/steamID32_once_logged')
    return steam_signin.RedirectUser(url)


@router.get('/steamID32_once_logged', name="steam:process-login")
async def get_steamID32_once_logged(request: Request, steam_signin: SteamSignIn = Depends(SteamSignIn)) -> int:
    steamid64 = steam_signin.ValidateResults(request.query_params)
    return int(steamid64) - 76561197960265728
