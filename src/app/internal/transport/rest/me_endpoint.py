import jwt
import ninja
from django.http import JsonResponse
from ninja.constants import NOT_SET
from ninja.security import HttpBearer
from ninja_extra import NinjaExtraAPI, api_controller, route
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

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
        return self.request.auth.user_id), json_dumps_params={"ensure_ascii": False})
