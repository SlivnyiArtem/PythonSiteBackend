import json

import environ
import requests
from django.http import HttpRequest, HttpResponse, JsonResponse

from app.internal.models.refresh_token import RefreshToken
from app.internal.models.simple_user import SimpleUser
from app.internal.services import token_service, user_service

env = environ.Env()
environ.Env.read_env()


def please_login(user: SimpleUser):
    return HttpResponse(
        json.dumps({"login": "please_login", "user_id": user.user_id}),
        content_type="application/json",
    )


class UserAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # response = self.get_response(request)
        return self.get_response(request)

    #     if "userapi" not in request.path:
    #         return self.get_response(request)
    #     raw_acc_token = None
    #
    #     # raw_acc_token = auth_data[1]
    #     # jwt_acc_token_data = token_service.get_token_data(raw_acc_token)
    #     user = user_service.get_user_by_id(request.headers["user_id"])
    #
    #     if user is None:
    #         pass
    #
    #     if raw_acc_token is None or token_service.check_is_token_expired(
    #         token_service.get_token_data(raw_acc_token), env("EXPIRE_TIME_ACCESS")
    #     ):
    #         refresh_token_obj = RefreshToken.objects.filter(user=user).first()
    #         if refresh_token_obj is None:
    #             return requests.post("https://flamberg.backend23.2tapp.cc/login/", request)
    #             # return HttpResponse("upd1")
    #         else:
    #             raw_refresh_token = refresh_token_obj.Jti
    #             refresh_token_data = token_service.get_token_data(raw_refresh_token)
    #             if token_service.check_is_token_expired(refresh_token_data, env("EXPIRE_TIME_REFRESH")):
    #                 token_service.revoke_all_tokens_for_user(user)
    #                 res_dict = requests.post("https://flamberg.backend23.2tapp.cc/login/", request)
    #                 return HttpResponse(res_dict)
    #             else:
    #                 token_service.revoke_all_tokens_for_user(user)
    #                 raw_refresh_token, raw_acc_token = token_service.create_tokens(user)
    #                 res_dict = token_service.get_json_dict_for_tokens(raw_refresh_token, raw_acc_token, user)
    #                 return HttpResponse(res_dict)
    #     else:
    #         return HttpResponse("ok")
    #
    #     # auth_response = authentificate(request, response)
    #     # if auth_response is None:
    #     # return response
    #     # return auth_response
    #
    # def process_view(self, request: HttpRequest, view_func, view_args, view_kwargs):
    #     # if "userapi" not in request.path:
    #     # return None
    #
    #     pass
    #     # Authoriz, user_id, psw
    #     # raw_acc_token = request.headers.get("Authorization")
    #
    #     #         else:
    #     #             raw_refresh_token = refresh_token_obj.Jti
    #     #             refresh_token_data = token_service.get_token_data(raw_refresh_token)
    #     #             if token_service.check_is_token_expired(refresh_token_data, env("EXPIRE_TIME_REFRESH")):
    #     #                 token_service.revoke_all_tokens_for_user(user)
    #     #                 requests.post("https://flamberg.backend23.2tapp.cc/login/", request)
    #     #                 return HttpResponse("upd2")
    #     #
    #     #             else:
    #     #                 token_service.revoke_all_tokens_for_user(user)
    #     #                 raw_refresh_token, raw_acc_token = token_service.create_tokens(user)
    #     #                 token_service.create_json_response_for_tokens(raw_refresh_token, raw_acc_token, user)
    #     #                 return HttpResponse("upd3")
    #     #                 # return HttpResponse(
    #     #                 #     json.dumps(
    #     #                 #         token_service.create_json_response_for_tokens(raw_refresh_token, raw_acc_token, user)
    #     #                 #     ),
    #     #                 #     content_type="application/json",
    #     #                 # )
    #
    #     # # return HttpResponse(request.headers)
    #     # #
    #     # # auth_data = request.META.get("HTTP_AUTHORIZATION").split()
    #     # # # token_str = auth_data[1]
    #     # # if auth_data[0] != "Token":
    #     # #     return HttpResponse(auth_data[0] + " " + "incorrect auth")
    #     # #
    #     # # # check expire
    #     # #
    #     # # return None
    #     # #
    #     # # # return None
    #     #
    #     # if "userapi" not in request.path:
    #     #     return None  # no changes
    #     # else:  # ! acc_token, user_id, password
    #     #     raw_acc_token = request.headers.get("acc_token")
    #     #     user = user_service.get_user_by_id(request.headers.get("user_id"))
    #     #     refresh_token_obj = RefreshToken.objects.filter(user=user).first()
    #     #
    #     #     if raw_acc_token is None or token_service.check_is_token_expired(
    #     #         token_service.get_token_data(raw_acc_token), env("EXPIRE_TIME_ACCESS")
    #     #     ):
    #     #         if refresh_token_obj is None:
    #     #             requests.post("https://flamberg.backend23.2tapp.cc/login/", request)
    #     #             return HttpResponse("upd1")
    #     #         else:
    #     #             raw_refresh_token = refresh_token_obj.Jti
    #     #             refresh_token_data = token_service.get_token_data(raw_refresh_token)
    #     #             if token_service.check_is_token_expired(refresh_token_data, env("EXPIRE_TIME_REFRESH")):
    #     #                 token_service.revoke_all_tokens_for_user(user)
    #     #                 requests.post("https://flamberg.backend23.2tapp.cc/login/", request)
    #     #                 return HttpResponse("upd2")
    #     #
    #     #             else:
    #     #                 token_service.revoke_all_tokens_for_user(user)
    #     #                 raw_refresh_token, raw_acc_token = token_service.create_tokens(user)
    #     #                 token_service.create_json_response_for_tokens(raw_refresh_token, raw_acc_token, user)
    #     #                 return HttpResponse("upd3")
    #     #                 # return HttpResponse(
    #     #                 #     json.dumps(
    #     #                 #         token_service.create_json_response_for_tokens(raw_refresh_token, raw_acc_token, user)
    #     #                 #     ),
    #     #                 #     content_type="application/json",
    #     #                 # )
    #     #     else:
    #     #         return HttpResponse("acc is ok")
