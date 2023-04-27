import datetime

import environ
import jwt
from django.http import HttpRequest

from app.internal.models.refresh_token import AuthToken
from app.internal.models.simple_user import SimpleUser
from app.internal.services import user_service

# from internal.models.access_token import AccessToken

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
            datetime.datetime.timestamp(datetime.datetime.now()),
            "access_token",
            user.hash_of_password,
            user.user_id,
        ),
        key=env("SECRET_FOR_TOKENS"),
        algorithm="HS512",
    )
    AuthToken.objects.update_or_create(jti=access_token, user=user, token_type="access")
    return access_token


def create_refresh_token(user: SimpleUser):
    refresh_token = jwt.encode(
        payload=create_payload(
            datetime.datetime.timestamp(datetime.datetime.now()),
            # datetime.datetime.timestamp(datetime.datetime.now() + datetime.timedelta(hours=1)) * 1000,
            "refresh_token",
            user.hash_of_password,
            user.user_id,
        ),
        key=env("SECRET_FOR_TOKENS"),
        algorithm="HS512",
    )
    AuthToken.objects.update_or_create(jti=refresh_token, user=user, token_type="refresh")
    # user = AuthToken.objects.filter(jti=refresh_token).values_list("user")
    return refresh_token


# def revoke__access_token(user: SimpleUser):
#     pass
#
#
# def revoke__refresh_token(user: SimpleUser):
#     pass


def update_and_get_tokens(user: SimpleUser):
    old_ref_token_jti = AuthToken.objects.filter(user=user, token_type="refresh").values_list("jti").first()
    old_acc_token_jti = AuthToken.objects.filter(user=user, token_type="access").values_list("jti").first()
    acc_token = create_access_token(user)
    ref_token = create_refresh_token(user)
    revoke_old_tokens(old_acc_token_jti, old_ref_token_jti)
    return acc_token, ref_token


def revoke_old_tokens(acc_jti, ref_jti):
    AuthToken.objects.filter(jti=acc_jti).delete()
    AuthToken.objects.filter(jti=ref_jti).delete()
