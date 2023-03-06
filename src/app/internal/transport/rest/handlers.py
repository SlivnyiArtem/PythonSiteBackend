from app.internal.transport.information_former import information_former
from django.http import JsonResponse


def me_http_inf_handler(_, user_id):
    information = information_former.try_get_information(user_id)
    return JsonResponse(information,
                        json_dumps_params={'ensure_ascii': False},
                        status=information["error_code"])
