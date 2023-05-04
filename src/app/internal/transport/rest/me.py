import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.internal.transport.information_former import form_information_handlers


class MeInfView(View):
    # request - user_id
    def get(self, request):
        user_id = 1299926658
        information = form_information_handlers.get_user_information(user_id)
        return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
        # # json_data = json.loads(request.body)
        # # user_id = json_data["user_id"]
        # return None
        # user_id = request.headers.get("user_id")
        # information = form_information_handlers.get_user_information(user_id)
        # return JsonResponse(information)
        # # response = HttpResponse(
        # #     json.dumps(information), content_type="application/json", status=information["error_code"]
        # # )
        # # response = JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
        # # response["user_id"] = str(user_id)
        # # return response
