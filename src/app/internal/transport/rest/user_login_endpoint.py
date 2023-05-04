import json

from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.internal.services import password_service, token_service, user_service


class UserLoginView(View):
    def post(self, request: HttpRequest):
        user = user_service.get_user_by_id(request.headers["user_id"])
        user_psw = request.headers["password"]
        if user_psw is None:
            return HttpResponseForbidden("Please set your password")
        if user is None:
            return HttpResponseForbidden("UserIsNone")

        if password_service.get_hash_from_password(user_psw) == user.hash_of_password:
            refresh_token, access_token = token_service.create_tokens(user)
            return JsonResponse({"auth": "correct", "refresh_token": refresh_token, "access_token": access_token})
        return HttpResponseForbidden("IncorrectPswd")
