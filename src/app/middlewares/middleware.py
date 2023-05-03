from django.http import JsonResponse


def auth_middleware(get_response):
    def auth(request):
        request_2 = request.GET.copy()
        request_2["mabooka"] = "great_mother"
        request.GET = request_2
        # response = get_response(request)

        return JsonResponse({"err": "err"}, status=404)

    return auth
