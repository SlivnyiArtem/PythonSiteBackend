import hashlib

from app.internal.users.db_data.models import AuthUser
from app.internal.users.presentation.entities import AuthUserSchema, TestInfSchema, UserInfSchema, UserSchema


class IUserRepository:
    def get_user_by_id(self, user_id: int) -> UserSchema:
        pass

    def get_user_by_username(self, username: str) -> UserSchema:
        pass

    def create_auth_user(self, user_id: int, password: str) -> AuthUserSchema:
        pass

    def update_create_user(self, user_id: int, default_updates: dict, auth_user: AuthUserSchema):
        pass

    def update_user_number(self, user_id: int, valid_phone_number) -> UserSchema:
        pass

    def update_auth_user_password(self, user_id, new_password: str) -> AuthUserSchema:
        pass

    def get_test_information(self):
        pass

    def get_me_information(self):
        pass


def get_hash_from_password(password: str) -> str:
    result = hashlib.sha512(password.encode("utf-8")).hexdigest()
    return result


class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def update_user_number(self, user_id: int, valid_phone_number: int):
        return self.user_repo.update_user_number(user_id=user_id, valid_phone_number=valid_phone_number)

    def update_create_user(self, user_id: int, default_updates: dict, auth_user: AuthUser):
        return self.user_repo.update_create_user(user_id, default_updates, auth_user)

    def update_user_password(self, user_id: int, password: str):
        return self.user_repo.update_auth_user_password(user_id=user_id, new_password=password)

    def get_user_by_id(self, user_id: int):
        return self.user_repo.get_user_by_id(user_id=user_id)

    def get_user_by_username(self, username: str):
        return self.user_repo.get_user_by_username(username=username)

    def create_auth_user(self, user_id: int, password: str):
        return self.user_repo.create_auth_user(user_id=user_id, password=password)

    # def update_user_number(user_id: int, phone_number: int):
    #     SimpleUser.objects.filter(simple_user_id=user_id).update(phone_number=phone_number)
    #
    # def update_create_user(user_id: int, default_updates: dict, auth_user: AuthUser):
    #     SimpleUser.objects.update_or_create(simple_user_id=user_id, user=auth_user, defaults=default_updates)
    #
    # def get_user_by_id(user_id: int) -> SimpleUser:
    #     result: SimpleUser = SimpleUser.objects.filter(simple_user_id=user_id).first()
    #     return result
    #
    # def get_user_by_username(username: str) -> SimpleUser:
    #     result: SimpleUser = SimpleUser.objects.filter(full_username=username).first()
    #     return result
    #
    # def create_auth_user(str_user_id: int, password: str) -> AuthUser:
    #     return AuthUser.objects.create_user(
    #         username=str(str_user_id),
    #         # email='jlennon@beatles.com',
    #         password=password,
    #     )
    #
    # def update_user_password(user_id: int, password: str):
    #     hash_of_password = get_hash_from_password(password)
    #     AuthUser.objects.filter(username=str(user_id)).update(password=hash_of_password)
    def get_me_information(self):
        return self.user_repo.get_me_information()

    def get_test_information(self):
        return self.user_repo.get_test_information()
