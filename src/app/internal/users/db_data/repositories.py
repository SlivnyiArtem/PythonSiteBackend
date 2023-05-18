from django.http import HttpResponse, JsonResponse

from app.internal.transport.information_former import form_information_handlers
from app.internal.users.application import user_service
from app.internal.users.db_data.models import AuthUser, SimpleUser
from app.internal.users.domain.services import IUserRepository, get_hash_from_password
from app.internal.users.presentation.entities import AuthUserSchema, UserSchema


class UserRepository(IUserRepository):
    def get_user_by_id(self, user_id: int) -> UserSchema:
        result: SimpleUser = SimpleUser.objects.filter(simple_user_id=user_id).first()
        return result

    def get_user_by_username(self, username: str) -> UserSchema:
        result: SimpleUser = SimpleUser.objects.filter(full_username=username).first()
        return result

    def create_auth_user(self, user_id: int, password: str) -> AuthUserSchema:
        return AuthUser.objects.create_user(
            username=str(user_id),
            password=password,
        )

    def update_create_user(self, user_id: int, default_updates: dict, auth_user: AuthUser) -> UserSchema:
        return SimpleUser.objects.update_or_create(simple_user_id=user_id, user=auth_user, defaults=default_updates)

    def update_user_number(self, user_id: int, valid_phone_number) -> UserSchema:
        return SimpleUser.objects.filter(simple_user_id=user_id).update(phone_number=valid_phone_number)

    def update_auth_user_password(self, user_id, new_password: str) -> AuthUserSchema:
        hash_of_password = get_hash_from_password(new_password)
        return AuthUser.objects.filter(username=str(user_id)).update(password=hash_of_password)

    def get_test_information(self, request):
        return HttpResponse("df")

    def get_me_information(self, request):
        information = user_service.get_user_information(request.user.username)
        return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])


# class Inf():
#     def __init__(self):
#         self.inf = "kjhkhj"
#
# class TestInf():
#     def __init__(self):
#         self.id = 34
