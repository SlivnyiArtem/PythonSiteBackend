from django.http import HttpResponse, JsonResponse
from ninja import Router, Schema
from ninja_jwt.authentication import JWTAuth

from app.internal.transport.information_former import form_information_handlers

rest_app_router = Router()


class Item(Schema):
    id: int


@rest_app_router.get("/me", auth=JWTAuth())
def me_handler(request):
    information = form_information_handlers.get_user_information(request.user.username)
    return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])


@rest_app_router.get("/test")
def test_handler(request):
    return HttpResponse("TESTTESTTEST")
