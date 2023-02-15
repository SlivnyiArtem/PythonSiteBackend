from django.http import JsonResponse
from app.internal.services import user_service


def me_http_inf_handler(_, user_id):
    return JsonResponse(user_service.try_get_information(user_id), json_dumps_params={'ensure_ascii': False})
