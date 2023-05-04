import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ninja import NinjaAPI
from ninja.security import HttpBearer, django_auth

from app.internal.transport.information_former import form_information_handlers
from app.internal.transport.rest.handlers import headers

api = NinjaAPI(csrf=True)


def check_is_token_ok(token):
    return False


class Auth(HttpBearer):
    def authenticate(self, request, token):
        if check_is_token_ok(token):
            return token


@api.get("/me", auth=Auth())
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
