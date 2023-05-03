from django.http import JsonResponse

from app.internal.services import token_service, user_service


def auth_middleware(get_response):
    def auth(request):
        # request_2 = request.GET.copy()
        # request_2["mabooka"] = "great_mother"
        # request.GET = request_2
        # content = {"err": "err"}

        response = get_response(request)

        user = user_service.get_user_by_id(response.context["user_id"])

        json_tokens_response = token_service.update_and_get_tokens(user)
        return json_tokens_response
        # return JsonResponse(tokens_response, status=404)

    return auth
