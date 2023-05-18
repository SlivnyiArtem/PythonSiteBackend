from rest_framework import status

# from app.internal.services import banking_service
# from app.internal.users.application import user_service
# from app.internal.users.db_data.models import SimpleUser


def get_currency_information(user_inf: dict, requisite_id: int) -> int:
    return 0
    # acc_inf = banking_service.get_acc_by_id(requisite_id)
    # card_inf = banking_service.get_card_by_id(requisite_id)
    # if card_inf is not None:
    #     if card_inf.banking_account.account_owner.simple_user_id != user_inf["simple_user_id"]:
    #         raise PermissionError("Доступ запрещен")
    #     return card_inf.banking_account.currency_amount
    # elif acc_inf is not None:
    #     if acc_inf.account_owner.simple_user_id != user_inf["simple_user_id"]:
    #         raise PermissionError("Доступ запрещен")
    #     return acc_inf.currency_amount


def get_user_information(user_id: int) -> dict:
    return {"A": 1}
    # user = user_service.get_user_by_id(user_id)
    # code = status.HTTP_200_OK
    # if user is None:
    #     code = status.HTTP_404_NOT_FOUND
    # elif user.phone_number is None:
    #     code = status.HTTP_403_FORBIDDEN
    # return SimpleUser.get_dictionary_deserialize(user, code)
