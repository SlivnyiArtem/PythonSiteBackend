from django.http import HttpResponse, JsonResponse

from app.internal.transport.information_former import form_information_handlers


def me_http_inf_handler(_, user_id: int):
    information = form_information_handlers.get_user_information(user_id)
    return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])


def test_page():
    return HttpResponse("<h1>connection established</h1>")
