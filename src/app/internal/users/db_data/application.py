from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth

from app.internal.users.db_data.controller import CustomController
from app.internal.users.presentation.entities import SimpleUserSchema
from app.internal.users.presentation.handlers import UserHandlers

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
from ninja import Router

from ninja_extra import api_controller
from ninja_jwt.controller import TokenObtainPairController


def get_users_router(user_handlers: UserHandlers):
    router = Router()

    @router.post("/me", auth=JWTAuth())
    def me_handler(request, user: SimpleUserSchema):
        return user_handlers.me_information(user)

    @router.get("/help")
    def test_handler(request):
        return user_handlers.help_information(request)

    @router.delete("/delete_user", auth=JWTAuth())
    def delete_user(request, user: SimpleUserSchema):
        return user_handlers.delete_user(user)

    return router


def get_api():
    api = NinjaExtraAPI()
    api.register_controllers(CustomController)
    user_handlers = UserHandlers()
    router = get_users_router(user_handlers)
    api.add_router("/users", router)
    return api

ninja_api= get_api()