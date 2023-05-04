import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.internal.transport.information_former import form_information_handlers
from app.internal.transport.rest.handlers import headers


@headers({"ttt": "ttt"})
class MeInfView(View):
    # request - user_id
    def get(self, request, user_id):
        # user_id = request.user_id
        # user_id = 1299926658
        return HttpResponse(request.ttt)
        information = form_information_handlers.get_user_information(user_id)
        return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
