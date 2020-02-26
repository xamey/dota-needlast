from pydantic import BaseModel


class MmrEstimate(BaseModel):
    estimate: int
    stdDev: int = None
    n: int = None


class Profile(BaseModel):
    account_id: int
    personaname: str
    name: str = None
    plus: bool = None
    cheese: int
    steamid: str
    avatar: str
    avatarmedium: str
    avatarfull: str
    profileurl: str
    last_login: str = None
    loccountrycode: str = None
    is_contributor: bool


class OpenDotaProfileInResponse(BaseModel):
    tracked_until: str = None
    solo_competitive_rank: str = None
    competitive_rank: str = None
    rank_tier: int = None
    leaderboard_rank: int = None
    mmr_estimate: MmrEstimate
    profile: Profile
