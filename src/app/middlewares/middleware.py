def auth_middleware(get_response):
    def auth(request):
        request_2 = request.GET.copy()
        request_2["mabooka"] = "great_mother"
        request.GET = request_2
        response = get_response(request)

        return response

    return auth
