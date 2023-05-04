import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.internal.services import password_service, token_service, user_service


class UserLoginView(View):
    def post(self, request: HttpRequest):
        json_data = json.loads(request.body)
        user = user_service.get_user_by_id(json_data["user_id"])
        # user_login = json_data["login"]
        user_psw = json_data["password"]

        if user is None:
            return JsonResponse({"user": "is_none"})

        if password_service.get_hash_from_password(user_psw) == user.hash_of_password:
            refresh_token, access_token = token_service.create_tokens(user)
            return JsonResponse({"auth": "correct", "refresh_token": refresh_token, "access_token": access_token})
        else:
            return JsonResponse({"auth": "incorrect"})
