def auth_middleware(get_response):
    def auth(request):
        raise Exception
        response = get_response(request)
        print("Check")
        return response

    return auth
