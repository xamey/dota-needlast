from pydantic import BaseModel


class UserBase(BaseModel):
    account_id: int
    region: str = None
    position: str = None
    language: str = None
    grade: str = None


class UserInDB(UserBase):
    last_login: str
    mmr: int = 0
    profile_pic: str


class UserOut(UserBase):
    last_login: str
    mmr: int = 0
    profile_pic: str

