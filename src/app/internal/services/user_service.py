from app.internal.models.auth_user import AuthUser
from app.internal.models.simple_user import SimpleUser
from app.internal.services.password_service import get_hash_from_password


def update_user_number(user_id: int, phone_number: int):
    SimpleUser.objects.filter(user_id=user_id).update(phone_number=phone_number)


def update_create_user(user_id: int, default_updates: dict):
    SimpleUser.objects.update_or_create(user_id=user_id, defaults=default_updates)


def get_user_by_id(user_id: int) -> SimpleUser:
    result: SimpleUser = SimpleUser.objects.filter(user_id=user_id).first()
    return result


def get_user_by_username(username: str) -> SimpleUser:
    result: SimpleUser = SimpleUser.objects.filter(full_username=username).first()
    return result


def create_auth_user(str_user_id: int) -> AuthUser:
    return AuthUser.objects.create_user(
        username=str(str_user_id),
        # email='jlennon@beatles.com',
        password="123",
    )


def update_user_password(user_id: int, password: str):
    hash_of_password = get_hash_from_password(password)
    SimpleUser.objects.filter(user_id=user_id).update(hash_of_password=hash_of_password)
