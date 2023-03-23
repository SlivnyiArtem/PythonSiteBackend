from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card


def get_card_by_id_and_user(card_number) -> Card:
    result: Card = Card.objects.filter(card_number=card_number).first()
    return result


def get_acc_by_id_and_user(acc_number) -> BankingAccount:
    result: BankingAccount = \
        BankingAccount.objects.filter(account_number=acc_number).first()
    return result
