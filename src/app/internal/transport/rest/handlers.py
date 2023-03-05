from app.internal.services import user_service
from django.http import JsonResponse


def me_http_inf_handler(_, user_id):
    information = user_service.try_get_information(user_id)
    return JsonResponse(information,
                        json_dumps_params={'ensure_ascii': False},
                        status=information["error_code"])
