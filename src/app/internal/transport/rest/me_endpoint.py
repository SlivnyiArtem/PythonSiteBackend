import json

import jwt
import ninja
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ninja.constants import NOT_SET
from ninja.security import HttpBearer, django_auth
from ninja_extra import NinjaExtraAPI, api_controller, route
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

from app.internal.transport.information_former import form_information_handlers
from app.internal.transport.rest.handlers import headers

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

router = ninja.Router()


class AuthBearer(HttpBearer):
    async def authenticate(self, request, token):
        return True


@api_controller(auth=NOT_SET, permissions=[])
class MyController:
    @route.get("/me", auth=JWTAuth())
    async def me(self):
        return JsonResponse(jwt.decode(self.request.auth), json_dumps_params={"ensure_ascii": False})
