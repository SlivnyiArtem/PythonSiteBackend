import json

import ninja
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ninja.security import HttpBearer, django_auth
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

from app.internal.transport.information_former import form_information_handlers
from app.internal.transport.rest.handlers import headers

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

router = ninja.Router()


@router.get("/me_endpoint", auth=JWTAuth())
def me_endpoint(request):
    information = form_information_handlers.get_user_information(47)
    return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])


def check_is_token_ok(token):
    return False
    # if "userapi" not in request.path:
    #     return self.get_response(request)
    # raw_acc_token = token
    #
    #     # raw_acc_token = auth_data[1]
    #     # jwt_acc_token_data = token_service.get_token_data(raw_acc_token)
    # user = user_service.get_user_by_id(request.headers["user_id"])
    #
    # if user is None:
    #     pass
    #
    # if raw_acc_token is None or token_service.check_is_token_expired(
    #     token_service.get_token_data(raw_acc_token), env("EXPIRE_TIME_ACCESS")
    # ):
    #     refresh_token_obj = RefreshToken.objects.filter(user=user).first()
    #     if refresh_token_obj is None:
    #         return requests.post("https://flamberg.backend23.2tapp.cc/login/", request)
    #             # return HttpResponse("upd1")
    #     else:
    #         raw_refresh_token = refresh_token_obj.Jti
    #         refresh_token_data = token_service.get_token_data(raw_refresh_token)
    #         if token_service.check_is_token_expired(refresh_token_data, env("EXPIRE_TIME_REFRESH")):
    #             token_service.revoke_all_tokens_for_user(user)
    #             res_dict = requests.post("https://flamberg.backend23.2tapp.cc/login/", request)
    #             return HttpResponse(res_dict)
    #         else:
    #             token_service.revoke_all_tokens_for_user(user)
    #             raw_refresh_token, raw_acc_token = token_service.create_tokens(user)
    #             res_dict = token_service.get_json_dict_for_tokens(raw_refresh_token, raw_acc_token, user)
    #             return HttpResponse(res_dict)
    # else:
    #     return HttpResponse("ok")
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


class Auth(HttpBearer):
    def authenticate(self, request, token):
        # if check_is_token_ok(token):
        if False:
            return token


def me(request, user_id):
    information = form_information_handlers.get_user_information(user_id)
    return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])


# class MeInfView(View):
#     # request - user_id
#
#     api = NinjaAPI(csrf=True)
#     @api.get("/bearer", auth=AuthBearer())
#     def get(self, request, user_id):
#         # user_id = request.user_id
#         # user_id = 1299926658
#         information = form_information_handlers.get_user_information(user_id)
#         return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
