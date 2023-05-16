from django.http import HttpResponse, JsonResponse
from ninja import Router, Schema
from ninja_jwt.authentication import JWTAuth

from app.internal.services import user_service
from app.internal.transport.rest.serializer import LoginSerializer, UserSerializer

rest_app_router = Router()


class Item(Schema):
    id: int


class LoginSchema(Schema):
    user_id: str
    password: str


# @rest_app_router.post("/test")
# def test(request, user_id: Item):
#     user = user_service.get_user_by_id(user_id.id)
#     serialized_user = UserSerializer(user).data
#     return JsonResponse({"user": serialized_user})


@rest_app_router.get("/me", auth=JWTAuth())
def me_handler(request):
    return HttpResponse("sdlkfj")


#
#
# def testo():
#     return HttpResponse("123213")
#
#
# @rest_app_router.get("/me2")
# def me_handler_2(request):
#     return HttpResponse("testudo")


@rest_app_router.post("/login")
def login(request, login_data: LoginSchema):
    # user = AuthUser.objects.filter(username=login_data.user_id).first()
    user_data = {"user_id": login_data.user_id, "password": login_data.password}
    serialized_log = LoginSerializer(data=user_data)
    res = serialized_log.is_valid(raise_exception=True)
    return HttpResponse(res)
    # return serialized_log.errors
    # return HttpResponse(res)


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
# @api_controller(auth=NOT_SET, permissions=[]) class MyController: @route.get("/me2", auth=JWTAuth()) async def me(
# self): return HttpResponse("sdlkfj") # user_id = self.request.auth.user_id # information =
# form_information_handlers.get_user_information(user_id) # return JsonResponse(information, json_dumps_params={
# "ensure_ascii": False}, status=information["error_code"])
