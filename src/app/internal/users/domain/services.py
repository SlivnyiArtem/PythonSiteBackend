import hashlib

from django.http import HttpResponse, JsonResponse
from rest_framework import status

from app.internal.users.db_data.models import AuthUser, SimpleUser
from app.internal.users.presentation.entities import AuthUserSchema, UserSchema


class IUserRepository:
    def get_user_by_id(self, user_id: int) -> UserSchema:
        pass

    def get_user_by_username(self, username: str) -> UserSchema:
        pass

    def create_auth_user(self, user_id: int, password: str) -> AuthUserSchema:
        pass

    def update_create_user(self, user_id: int, default_updates: dict, auth_user: AuthUser):
        pass

    def update_user_number(self, user_id: int, valid_phone_number) -> UserSchema:
        pass

    def update_auth_user_password(self, user_id, new_password: str) -> AuthUserSchema:
        pass

    # def get_test_information(self):
    #     pass
    #
    # def get_me_information(self, user_id):
    #     pass
    def delete_user(self, user_id):
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

    def get_me_information(self, user_id):
        user = self.get_user_by_id(user_id)
        user_obj = SimpleUser.objects.filter(simple_user_id=user.simple_user_id).first()
        information = SimpleUser.get_dictionary_deserialize(user_obj, status.HTTP_200_OK)
        # user_obj = user
        # information = {"MQ": 42}
        # information = user_service.get_user_information(request.user.username)
        return JsonResponse(
            information,
            json_dumps_params={"ensure_ascii": False},
            # status=information["error_code"]
        )

    def get_test_information(self):
        return HttpResponse("df")

    def delete_user(self, user_id):
        return self.user_repo.delete_user(user_id=user_id)
