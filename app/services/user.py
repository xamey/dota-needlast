from app.models.domain.open_dota_profile.OpenDotaProfile import OpenDotaProfile
from app.models.domain.users.User import UserInDB


def create_empty_user_from_open_dota_profile(open_dota_profile: OpenDotaProfile):
    print(open_dota_profile)
    return UserInDB(
        last_login="Today",
        mmr=open_dota_profile.mmr_estimate.estimate,
        profile_pic=open_dota_profile.profile.avatar,
        account_id=open_dota_profile.profile.account_id,
        language=open_dota_profile.profile.loccountrycode,
        grade=open_dota_profile.competitive_rank
    )
