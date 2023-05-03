import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.views import APIView

from app.internal.services import token_service, user_service
from app.internal.transport.information_former import form_information_handlers


def headers(headers_dict):
    def wrapper(orig_func):
        def inner_wrapper(*args, **kwargs):
            response = orig_func(*args, **kwargs)
            for key, val in headers_dict.iteritems():
                response[key] = val
            return response

        return inner_wrapper

    return wrapper


def me_http_inf_handler(_, user_id: int):
    information = form_information_handlers.get_user_information(user_id)
    response = HttpResponse(json.dumps(information), content_type="application/json", status=information["error_code"])
    # response = JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
    response["user_id"] = str(user_id)
    return response


# def me_endpoint(user_id: int):
#     information = form_information_handlers.get_user_information(user_id)
#     response = JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
#     response["user_id"] = user_id
#     return response


def test_page(_):
    return HttpResponse("<h1>connection established</h1>")


class LoginView(APIView):
    def post(self, request: HttpRequest):
        json_data = json.loads(request.body.decode("utf-8"))
        user = user_service.get_user_by_id(json_data["user_id"])
        access_token, refresh_token = token_service.update_and_get_tokens(user)
        # refresh_token = token_service.create_refresh_token(user)
        # access_token = token_service.create_access_token(user)
        return JsonResponse({"refresh_token": refresh_token, "access_token": access_token})
        # return JsonResponse({"test1": "test1_v", "test2": "test2_v"})
