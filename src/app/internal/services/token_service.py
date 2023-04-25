import environ
import jwt
from internal.models.simple_user import SimpleUser
from internal.models.token import RefreshToken

env = environ.Env()
environ.Env.read_env()


def create_payload(time_to_expire, token_type, user_hash_password, user_id):
    return {
        "time_to_expire": time_to_expire,
        "token_type": token_type,
        "user_id": user_id,
        "user_hash_password": user_hash_password,
    }


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


def revoke_refresh_token(jti):
    RefreshToken.objects.filter(jti=jti).delete()
    pass
