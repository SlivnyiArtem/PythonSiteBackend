import environ
from django.http import HttpRequest, JsonResponse

from internal.models.refresh_token import RefreshToken
from internal.services import user_service, token_service

env = environ.Env()
environ.Env.read_env()


def auth_middleware(get_response):
    def auth(request: HttpRequest):
        # return get_response(request)

        if "userapi" not in request.path:
            return get_response(request)

        # проверка наличия и актуальности токенов
        # пустой payload, просроченный токен,отсутствующий токен

        user = user_service.get_user_by_id(request.headers.get("user_id"))
        if user is None:
            pass
        raw_acc_token = request.headers.get("acc_token")

        refresh_token_obj = RefreshToken.objects.filter(user=user).first()
        raw_refresh_token = refresh_token_obj.Jti
        refresh_token_data = token_service.get_token_data(raw_refresh_token)

        # если асс-токена нет или он просрочен
        if raw_acc_token is None or token_service.check_is_token_expired(
            token_service.get_token_data(raw_acc_token), env("EXPIRE_TIME_ACCESS")
        ):
            if refresh_token_obj is None:
                return JsonResponse({"Login": "Логинься"})
                pass
            elif token_service.check_is_token_expired(refresh_token_data, env("EXPIRE_TIME_REFRESH")):
                token_service.revoke_all_tokens_for_user(user)
                return JsonResponse({"Login": "Логинься"})
                pass
            else:
                raw_refresh_token, raw_acc_token = token_service.update_and_get_tokens(user, refresh_token_obj)

            # 1.  проверка refresh, если валиден, то запрос с сервера нового access_токена(передавая рефреш),
            #    обновление рефреш токена, отзыв старого токена
            # 2.    если не валиден - отзыв старого токена, перенаправление на ввод пароля
            # 3.    если отсутствует - перенаправление на ввод пароля

        else:
            # все ок, наш токен свежий
            pass

        return token_service.create_json_response_for_tokens(raw_refresh_token, raw_acc_token, user)

    return auth
