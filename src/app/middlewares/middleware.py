from django.http import JsonResponse

from app.internal.services import token_service


def auth_middleware(get_response):
    def auth(request):
        # request_2 = request.GET.copy()
        # request_2["mabooka"] = "great_mother"
        # request.GET = request_2
        # content = {"err": "err"}

        json_tokens_response = token_service.update_and_get_tokens()
        return json_tokens_response
        # return JsonResponse(tokens_response, status=404)

    return auth
