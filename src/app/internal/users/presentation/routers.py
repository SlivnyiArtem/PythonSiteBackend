from ninja import Router
from ninja_jwt.authentication import JWTAuth

from app.internal.users.presentation.entities import UserSchema
from app.internal.users.presentation.handlers import UserHandlers


def get_users_router(user_handlers: UserHandlers):
    router = Router()

    @router.get("/me", auth=JWTAuth())
    def me_handler(request):
        return user_handlers.me_information(request)

    @router.get("/test")
    def test_handler(request):
        return user_handlers.test_information()

    @router.get("/transactions", auth=JWTAuth())
    def transactions_log_handler(request):
        return user_handlers.get_transactions_log(request)

    @router.put("/create_user", auth=JWTAuth())
    def create_user(user: UserSchema):
        return user_handlers.create_user(user)

    @router.delete("/delete_user", auth=JWTAuth())
    def delete_user(user: UserSchema):
        return user_handlers.delete_user(user)

    return router


# rest_app_router = Router()
#
#
# @router.get("/me", auth=JWTAuth())
# def me_handler(request):
#     # information = form_information_handlers.get_user_information(request.user.username)
#     information = {"2": "@"}
#     return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
#
#
# @router.get("/test")
# def test_handler(request):
#     return HttpResponse("TESTTESTTEST")
