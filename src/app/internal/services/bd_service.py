from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card
from app.internal.models.simple_user import SimpleUser


def get_user_by_id(user_id) -> SimpleUser:
    result: SimpleUser = SimpleUser. \
        objects.filter(user_id=user_id).first()
    return result


def get_card_by_id_and_user(card_number) -> Card:
    result: Card = Card.objects.filter(card_number=card_number).first()
    return result


def get_acc_by_id_and_user(acc_number) -> BankingAccount:
    result: BankingAccount = BankingAccount.objects.filter(account_number=acc_number).first()
    return result
