def auth_middleware(get_response):
    def auth(request):
        raise Exception
        print("Check")
        response = get_response(request)
        return response

    return auth
