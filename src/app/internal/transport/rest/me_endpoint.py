from datetime import datetime
from typing import Optional

from django.http import HttpResponse, JsonResponse
from ninja import ModelSchema, Router, Schema
from ninja_jwt import schema
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.tokens import SlidingToken

from app.internal.models.simple_user import SimpleUser
from app.internal.services import user_service
from app.internal.transport.rest.serializer import UserSerializer

rest_app_router = Router()


class Item(Schema):
    id: int


@rest_app_router.post("/test")
def test(request, user_id: Item):
    user = user_service.get_user_by_id(user_id.id)
    serialized_user = UserSerializer(user).data
    return JsonResponse({"user": serialized_user})


@rest_app_router.get("/me", auth=JWTAuth())
def me_handler():
    return HttpResponse("sdlkfj")


#
# class UserRetrieveSchema(ModelSchema):
#     # groups: List[GroupSchema]
#     class Config:
#         model = SimpleUser
#         model_fields = ["user_id"]
#
# class UserTokenOutSchema(Schema):
#     token: str
#     user: UserRetrieveSchema
#     token_exp_date: Optional[datetime]
#
#
# @rest_app_router.post("/login", response=UserTokenOutSchema, url_name="login")
# def obtain_token(user_token: schema.TokenObtainSlidingSerializer):
#     user = user_token._user
#     token = SlidingToken.for_user(user)
#     return UserTokenOutSchema(
#         user=user,
#         token=str(token),
#         token_exp_date=datetime.utcfromtimestamp(token["exp"]),
#     )
#
#
# @rest_app_router.post(
#     "/api-token-refresh",
#     response=schema.TokenRefreshSlidingSerializer,
#     url_name="refresh",
# )
# def refresh_token(refresh_token: schema.TokenRefreshSlidingSchema):
#     refresh = schema.TokenRefreshSlidingSerializer(**refresh_token.dict())
#     return refresh

# from app.internal.transport.information_former import form_information_handlers
#
# api = NinjaExtraAPI()
# api.register_controllers(NinjaJWTDefaultController)
#
# router = ninja.Router()
#
#
# def me(request, user_id):
#     information = form_information_handlers.get_user_information(user_id)
#     return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
#
#
# class AuthBearer(HttpBearer):
#     async def authenticate(self, request, token):
#         return True
#
#
# @api_controller(auth=NOT_SET, permissions=[])
# class MyController:
#     @route.get("/me2", auth=JWTAuth())
#     async def me(self):
#         return HttpResponse("sdlkfj")
#         # user_id = self.request.auth.user_id
#         # information = form_information_handlers.get_user_information(user_id)
#         # return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
