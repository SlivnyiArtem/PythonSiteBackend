def auth_middleware(get_response):
    def auth(request):
        request.META["mabooka"] = "mother"
        return get_response(request)
        # return response

    return auth
