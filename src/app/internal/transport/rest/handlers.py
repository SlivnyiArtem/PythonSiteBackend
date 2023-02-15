from django.http import JsonResponse
from rfc3986.compat import unicode

from app.internal.models.simple_user import SimpleUser


def me_http_inf_handler(_, user_id):
    result: SimpleUser = SimpleUser.objects.filter(user_id=user_id).first()
    if result is None:
        return JsonResponse({"error_message":"Пользователь отсутствует в базе данных. "
                                             "Попробуйте создать его в telegram_боте с помощью команды /start"})
    else:
        dict = result.get_dictionary_deserialize()
        '''
        dict.pop("_state")
        print(dict)
        for key in dict.keys():
            value = dict[key]
            if type(value) != str:
                continue
            value = value.encode('utf-8').decode('raw-unicode-escape')
            dict.pop(key)
            dict[key] = value
            # if not value.isdigit():
                # value = value.decode('raw-unicode-escape').encode('utf-8')

        print(result.get_dictionary_deserialize().items())
        # print({k: unicode(v).encode("utf-8") for k, v in dict.items()})



        # return JsonResponse({k: v.decode('raw-unicode-escape').encode('utf-8') for k, v in dict.items()})
        '''
        return JsonResponse(dict, json_dumps_params={'ensure_ascii': False})
