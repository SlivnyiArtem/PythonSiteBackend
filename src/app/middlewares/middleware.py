# import json
#
# import environ
# import requests
# from django.http import HttpRequest, HttpResponse, JsonResponse
#
# from app.internal.models.refresh_token import RefreshToken
# from app.internal.models.simple_user import SimpleUser
# from app.internal.services import token_service, user_service
#
# env = environ.Env()
# environ.Env.read_env()
#
#
# def please_login(user: SimpleUser):
#     return HttpResponse(
#         json.dumps({"login": "please_login", "user_id": user.simple_user_id}),
#         content_type="application/json",
#     )
#


class UserAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
