import json


def auth_middleware(get_response):
    def auth(request):
        # request_2 = request.GET.copy()

        request_data = getattr(request, "_body", request.body)
        request_data = json.loads(request_data)

        request_data["mabooka"] = "great_mother"
        # here you can write the logic to append the payload to request data
        request._body = json.dumps(request_data)

        # request_2["mabooka"] = "great_mother"
        # request.GET = request_2
        response = get_response(request)

        return response

    return auth
