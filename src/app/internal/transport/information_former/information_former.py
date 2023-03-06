from rest_framework import status
from app.internal.models.simple_user import SimpleUser
from app.internal.transport.messages import common_messages


def try_get_information(user_id):
    result: SimpleUser = SimpleUser. \
        objects.filter(user_id=user_id).first()
    if result is None:
        return {"error_message":
                common_messages.no_information_in_db_message(),
                "error_code": status.HTTP_404_NOT_FOUND}
    elif result.phone_number is None:
        return {"error_message":
                common_messages.access_restricted_message(),
                "error_code": status.HTTP_403_FORBIDDEN}
    else:
        res = result.get_dictionary_deserialize()
        res.update(error_code=status.HTTP_200_OK)
        return res
