from app.internal.models.auth_user import AuthUser
from app.internal.models.simple_user import SimpleUser
from app.internal.services.password_service import get_hash_from_password


def update_user_number(user_id: int, phone_number: int):
    SimpleUser.objects.filter(simple_user_id=user_id).update(phone_number=phone_number)


def update_create_user(user_id: int, default_updates: dict, auth_user: AuthUser):
    SimpleUser.objects.update_or_create(simple_user_id=user_id, user=auth_user, defaults=default_updates)


def get_user_by_id(user_id: int) -> SimpleUser:
    result: SimpleUser = SimpleUser.objects.filter(simple_user_id=user_id).first()
    return result


def get_user_by_username(username: str) -> SimpleUser:
    result: SimpleUser = SimpleUser.objects.filter(full_username=username).first()
    return result


def create_auth_user(str_user_id: int, password: str) -> AuthUser:
    return AuthUser.objects.create_user(
        username=str(str_user_id),
        # email='jlennon@beatles.com',
        password=password,
    )


def update_user_password(user_id: int, password: str):
    hash_of_password = get_hash_from_password(password)
    AuthUser.objects.filter(username=str(user_id)).update(password=hash_of_password)
