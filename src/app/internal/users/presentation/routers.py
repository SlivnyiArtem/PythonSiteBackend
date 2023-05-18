from ninja import Router
from ninja_jwt.authentication import JWTAuth

from app.internal.users.presentation.handlers import UserHandlers


def get_users_router(user_handlers: UserHandlers):
    router = Router()

    @router.get("/me", auth=JWTAuth())
    def me_handler(request):
        return user_handlers.me_information(request)

    @router.get("/test")
    def test_handler(request):
        return user_handlers.test_information(request)

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
