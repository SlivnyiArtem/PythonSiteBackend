from app.internal.transport.information_former import form_information_handlers
from django.http import JsonResponse


def me_http_inf_handler(_, user_id):
    information = form_information_handlers.get_information(user_id)
    return JsonResponse(information,
                        json_dumps_params={'ensure_ascii': False},
                        status=information["error_code"])
