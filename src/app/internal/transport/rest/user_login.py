import json

from django.http import HttpRequest, JsonResponse
from django.views import View

from internal.services import user_service, password_service, token_service


class UserLoginView(View):
    def post(self, request: HttpRequest):

        json_data = json.loads(request.body)
        user = user_service.get_user_by_id(json_data["user_id"])
        # user_login = json_data["login"]
        user_psw = json_data["password"]

        if user is None:
            pass

        if (password_service.get_hash_from_password(user_psw)
                == user.hash_of_password):
            refresh_token, access_token = token_service.create_tokens(user)
            return JsonResponse({"refresh_token": refresh_token, "access_token": access_token})
        else:
            pass






        login = request.POST["login"]
        password = request.POST["password"]

        if not is_user_exist(login):
            return HttpResponse("401 Unauthorized", status=401)
        user = get_user(login)
        password_hash = get_hash(password)
        expected_hash = bytes(user.password_hash)
        if expected_hash != password_hash:
            return HttpResponseForbidden()

        revoke_tokens(user)
        access_token, refresh_token = generate_access_and_refresh_tokens(user)
        return JsonResponse({"access_token": access_token, "refresh_token": refresh_token})
