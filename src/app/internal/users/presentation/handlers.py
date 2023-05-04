from django.http import HttpResponse, JsonResponse
from ninja_extra import status

from app.internal.models.simple_user import SimpleUser
from app.internal.models.transaction import Transaction
from app.internal.services.user_service import get_user_by_id
from app.internal.transport.messages.common_messages import help_command_message
from app.internal.users.presentation.entities import SimpleUserSchema


# from app.internal.users.domain.services import UserService
# from app.internal.users.presentation.entities import SimpleUserSchema, UserSchema


class UserHandlers:
    # def __init__(self, user_service: UserService):
    #     self._user_service = user_service

    def me_information(self, user_schema: SimpleUserSchema):
        user = get_user_by_id(user_schema.simple_user_id)
        information = SimpleUser.get_dictionary_deserialize(user, status.HTTP_200_OK)
        return JsonResponse(
            information,
            json_dumps_params={"ensure_ascii": False},
        )


        # user = get_user_by_id(request.user.username)
        # user_obj = SimpleUser.objects.filter(simple_user_id=user.simple_user_id).first()
        # information = SimpleUser.get_dictionary_deserialize(user_obj, status.HTTP_200_OK)
        # return JsonResponse(
        #     information,
        #     json_dumps_params={"ensure_ascii": False},
        # )
    def help_information(self, request):
        return JsonResponse(
            {"help_msg": help_command_message()},
            json_dumps_params={"ensure_ascii": False},
        )
        # common_messages.help_command_message()
        # return self._user_service()

    def delete_user(self, user_schema: SimpleUserSchema):
        user = get_user_by_id(user_schema.simple_user_id)
        # user = SimpleUser.objects.filter(username=user_id).first()
        user.delete()
        return HttpResponse(
            "Пользователь удален")
