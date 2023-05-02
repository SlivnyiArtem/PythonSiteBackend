def auth_middleware(get_response):
    def auth(request):
        response = get_response(request)
        response["mabooka"] = "mother"
        # return response

    return auth
