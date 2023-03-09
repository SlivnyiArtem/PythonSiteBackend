from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card
from app.internal.models.simple_user import SimpleUser
from app.internal.transport.messages import common_messages
from rest_framework import status


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


def try_get_user(user_id):
    result: SimpleUser = SimpleUser. \
        objects.filter(user_id=user_id).first()
    return result


def try_get_card_information(user, card_id):
    result_1: Card = Card. \
        objects.filter(card_number=card_id)\
        .filter(card_owner=user).first()
    result_2: BankingAccount = BankingAccount. \
        objects.filter(account_number=card_id)\
        .filter(account_owner=user).first()
    if result_1 is not None:
        return result_1.currency_amount
    elif result_2 is not None:
        return result_2.currency_amount
    else:
        return None
