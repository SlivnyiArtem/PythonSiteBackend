from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.views import APIView

from app.internal.transport.information_former import form_information_handlers


def me_http_inf_handler(_, user_id: int):
    information = form_information_handlers.get_user_information(user_id)
    return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])


def test_page(_):
    return HttpResponse("<h1>connection established</h1>")


class LoginView(APIView):
    def post(self, request: HttpRequest):
        return JsonResponse({"test1": "test1_v", "test2": "test2_v"})
