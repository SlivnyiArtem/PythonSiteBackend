from django.http import JsonResponse
from app.internal.services import user_service


def me_http_inf_handler(_, user_id):
    information = user_service.try_get_information(user_id)
    return JsonResponse(information, json_dumps_params={'ensure_ascii': False}, status=information["error_code"])


    # res = JsonResponse(information, json_dumps_params={'ensure_ascii': False},
    #                    status=status_code)
    # # res = JsonResponse(user_service.try_get_information(user_id), json_dumps_params={'ensure_ascii': False},
    # #                    status=status.HTTP_404_NOT_FOUND)
    # print(res.status_code)
    # return res
    # # return JsonResponse(user_service.try_get_information(user_id), json_dumps_params={'ensure_ascii': False})
