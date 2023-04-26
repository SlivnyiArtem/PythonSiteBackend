import environ
import jwt
from django.http import HttpRequest
from internal.models.simple_user import SimpleUser
from internal.models.token import RefreshToken
from internal.services import user_service

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
def create_access_token(refresh_token: RefreshToken, user: SimpleUser) -> str:
    if refresh_token.user == user:
        access_token = jwt.encode(
            payload=create_payload(env("ACCESS_EXPIRE"), "access_token", user.hash_of_password, user.user_id),
            key=env("SECRET_FOR_TOKENS"),
            algorithm="HS512",
        )
        return access_token


def create_refresh_token(device_id, user: SimpleUser):
    refresh_token = jwt.encode(
        payload=create_payload(env("REFRESH_EXPIRE"), "refresh_token", user.hash_of_password, user.user_id),
        key=env("SECRET_FOR_TOKENS"),
        algorithm="HS512",
    )
    RefreshToken.objects.create(jti=refresh_token, device_id=device_id, user=user)
    return refresh_token


def revoke__access_token(user: SimpleUser):
    pass


def revoke__refresh_token(user: SimpleUser):
    pass


def update_tokens(user: SimpleUser, refresh_token):
    create_access_token()
    create_refresh_token()


def revoke_refresh_token(jti):
    RefreshToken.objects.filter(jti=jti).delete()
    pass
