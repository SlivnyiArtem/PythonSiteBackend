from rest_framework import status

from app.internal.models.simple_user import SimpleUser
from app.internal.services import banking_service, user_service


def get_currency_information(user: SimpleUser, requisite_id: int) -> int:
    acc_inf = banking_service.get_acc_by_id_and_user(requisite_id)
    card_inf = banking_service.get_card_by_id_and_user(requisite_id)
    if card_inf is not None:
        if card_inf.banking_account.account_owner.user_id != user["user_id"]:
            raise PermissionError("Доступ запрещен")
        return card_inf.banking_account.currency_amount
    elif acc_inf is not None:
        if acc_inf.account_owner.user_id != user["user_id"]:
            raise PermissionError("Доступ запрещен")
        return acc_inf.currency_amount


def get_user_information(user_id: int) -> dict:
    user = user_service.get_user_by_id(user_id)
    code = status.HTTP_200_OK
    if user is None:
        code = status.HTTP_404_NOT_FOUND
    elif user.phone_number is None:
        code = status.HTTP_403_FORBIDDEN
    return SimpleUser.get_dictionary_deserialize(user, code)
