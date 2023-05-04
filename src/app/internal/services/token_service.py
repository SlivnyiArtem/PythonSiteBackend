import datetime

import environ
import jwt
from django.http import JsonResponse

from app.internal.models.refresh_token import RefreshToken
from app.internal.models.simple_user import SimpleUser

env = environ.Env()
environ.Env.read_env()


def get_token_data(token: str):
    return jwt.decode(token, key=env("SECRET_FOR_TOKENS"), algorithms=["HS512"])


def check_is_expired_refresh_token_obj(auth_token: RefreshToken):
    # token_data = get_token_data(auth_token.Jti)
    return check_is_token_expired(get_token_data(auth_token.Jti), env("EXPIRE_TIME_REFRESH"))

    # return datetime.datetime.timestamp(datetime.datetime.now()) - token_data["start_time"] > float(
    #     env("EXPIRE_TIME_REFRESH")
    # )


def check_is_token_expired(token_data: dict, expire_time: str):
    return datetime.datetime.timestamp(datetime.datetime.now()) - token_data["start_time"] > float(expire_time)


def create_payload(start_time, token_type, user_hash_password, user_id):
    return {
        "start_time": start_time,
        "token_type": token_type,
        "user_id": user_id,
        "user_hash_password": user_hash_password,
    }


def create_access_token(user: SimpleUser) -> str:
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
    # AuthToken.objects.create(Jti=access_token, user=user, token_type="access")
    return access_token


# def update_refresh_tokens(user: SimpleUser):
#     revoke_all_tokens_for_user(user)
#     create_refresh_token(user)


def create_refresh_token(user: SimpleUser):
    refresh_token = jwt.encode(
        payload=create_payload(
            datetime.datetime.timestamp(datetime.datetime.now()),
            "refresh_token",
            user.hash_of_password,
            user.user_id,
        ),
        key=env("SECRET_FOR_TOKENS"),
        algorithm="HS512",
    )
    RefreshToken.objects.create(Jti=refresh_token, user=user)
    return refresh_token


# def update_and_get_tokens(user: SimpleUser):  # THERE
#     old_ref_token_jti = AuthToken.objects.filter(user=user, token_type="refresh").values_list("Jti").first()
#     old_acc_token_jti = AuthToken.objects.filter(user=user, token_type="access").values_list("Jti").first()
#     acc_token = create_access_token(user)
#     ref_token = create_refresh_token(user)
#     revoke_old_tokens(old_acc_token_jti, old_ref_token_jti)
#     return acc_token, ref_token


def revoke_old_tokens(jti):
    RefreshToken.objects.filter(Jti=jti).delete()


def revoke_all_tokens_for_user(user: SimpleUser):
    # AuthToken.objects.filter(user=user, token_type="refresh").delete()
    # AuthToken.objects.filter(user=user, token_type="access").delete()
    RefreshToken.objects.filter(user=user).delete()


def create_tokens(user: SimpleUser):
    # revoke_all_tokens_for_user(user)
    access_token = create_access_token(user)
    refresh_token, _ = create_refresh_token(user)

    return refresh_token, access_token


# def create_json_response_for_tokens(raw_refresh_tokem: str, raw_access_token: str, user: SimpleUser):
#     if user.login_access:
#         return JsonResponse({"status": True, "refresh_token": raw_refresh_tokem, "access_token": raw_access_token})
#     else:
#         return JsonResponse({"status": False})


def create_json_response_for_tokens(raw_refresh_tokem: str, raw_access_token: str, user: SimpleUser):
    if user.login_access:
        return {"status": True, "refresh_token": raw_refresh_tokem, "access_token": raw_access_token}
    else:
        return {"status": False}
