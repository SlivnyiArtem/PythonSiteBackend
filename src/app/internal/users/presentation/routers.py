from ninja import Router
from ninja_jwt.authentication import JWTAuth

from app.internal.users.presentation.handlers import UserHandlers


def get_users_router(user_handlers: UserHandlers):
    router = Router()

    # router.add_api_operation(
    #     path="/me", auth=JWTAuth(), methods=["GET"], response={}, view_func=user_handlers.me_information
    # )
    #
    router.add_api_operation(path="/test", methods=["GET"], response={}, view_func=user_handlers.test_information)

    return router


# rest_app_router = Router()
#
#
# @rest_app_router.get("/me", auth=JWTAuth())
# def me_handler(request):
#     information = form_information_handlers.get_user_information(request.user.username)
#     return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
#
#
# @rest_app_router.get("/test")
# def test_handler(request):
#     return HttpResponse("TESTTESTTEST")
