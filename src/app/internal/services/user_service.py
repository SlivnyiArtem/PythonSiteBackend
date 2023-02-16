from app.internal.models.simple_user import SimpleUser
from app.internal.transport.messages import common_messages


def update_user_number(user_id, number):
    SimpleUser.objects.filter(user_id=user_id).update(phone_number=number)


def update_create_user(user_id, default_updates):
    SimpleUser.objects.update_or_create(user_id=user_id, defaults=default_updates)


def try_get_information(user_id):
    result: SimpleUser = SimpleUser.objects.filter(user_id=user_id).first()
    if result is None:
        return {"error_message": common_messages.no_information_in_db_message()}
    elif result.phone_number is None:
        return {"error_message": common_messages.access_restricted_message()}
    else:
        return result.get_dictionary_deserialize()


def dict_ser_to_str_ser(input_dict):
    result_str = ""
    for key, value in input_dict.items():
        result_str += str(key) + " : " + str(value) + "\n"
    return result_str
