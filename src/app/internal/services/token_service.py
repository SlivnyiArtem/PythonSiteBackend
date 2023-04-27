import datetime

import environ
import jwt
from django.http import HttpRequest

from app.internal.models.simple_user import SimpleUser
from app.internal.models.token import RefreshToken
from app.internal.services import user_service

env = environ.Env()
environ.Env.read_env()


def authentificate(token, http_request: HttpRequest):
    payload = jwt.decode(token, env("JWT_SECRET"), algorithms=["HS512"])
    user_id = payload["user_id"]
    user = user_service.get_user_by_id(user_id)
    if user is not None:
        pass
    else:
        pass


def create_payload(time_to_expire, token_type, user_hash_password, user_id):
    return {
        "time_to_expire": time_to_expire,
        "token_type": token_type,
        "user_id": user_id,
        "user_hash_password": user_hash_password,
    }


# посмотреть как задается expired
# после залогинивания, мы создаем accessToken на основе refresh
# Создаём новый refrsh token?????
def create_access_token(user: SimpleUser) -> str:
    # if refresh_token_user == user:
    access_token = jwt.encode(
        payload=create_payload(
            datetime.datetime.timestamp(datetime.datetime.now() + datetime.timedelta(hours=1)) * 1000,
            "access_token",
            user.hash_of_password,
            user.user_id,
        ),
        key=env("SECRET_FOR_TOKENS"),
        algorithm="HS512",
    )
    return access_token


def create_refresh_token(user: SimpleUser):
    refresh_token = jwt.encode(
        payload=create_payload(
            datetime.datetime.timestamp(datetime.datetime.now() + datetime.timedelta(hours=1)) * 1000,
            "refresh_token",
            user.hash_of_password,
            user.user_id,
        ),
        key=env("SECRET_FOR_TOKENS"),
        algorithm="HS512",
    )
    RefreshToken.objects.update_or_create(jti=refresh_token, user=user)
    user = RefreshToken.objects.filter(jti=refresh_token).values_list("user")
    return refresh_token


# def revoke__access_token(user: SimpleUser):
#     pass
#
#
# def revoke__refresh_token(user: SimpleUser):
#     pass


def update_tokens(user: SimpleUser):
    old_ref_token_jti = RefreshToken.objects.filter(user=user).first().values_list("jti")
    acc_token = create_access_token(user)
    ref_token = create_refresh_token(user)
    if old_ref_token_jti is not None:
        revoke_refresh_token(old_ref_token_jti)


def revoke_refresh_token(jti):
    RefreshToken.objects.filter(jti=jti).delete()
