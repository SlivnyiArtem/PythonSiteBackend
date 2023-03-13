from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card
from app.internal.models.simple_user import SimpleUser


def get_user_by_id(user_id):
    result: SimpleUser = SimpleUser. \
        objects.filter(user_id=user_id).first()
    return result


def get_card_by_id_and_user(user_id, card_number):
    result: Card = Card. \
        objects.filter(card_number=card_number) \
        .filter(card_owner=user_id).first()
    return result


def get_acc_by_id_and_user(user_id, acc_number):
    result: BankingAccount = BankingAccount. \
        objects.filter(account_number=acc_number) \
        .filter(account_owner=user_id).first()
    return result
