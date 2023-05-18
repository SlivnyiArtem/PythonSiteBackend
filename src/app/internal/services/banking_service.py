from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card
from app.internal.users.application import user_service


def get_card_by_id(card_number: int) -> Card:
    result: Card = Card.objects.filter(card_number=card_number).first()
    return result


def get_acc_by_id(acc_number: int) -> BankingAccount:
    result: BankingAccount = BankingAccount.objects.filter(account_number=acc_number).first()
    return result


def get_acc_by_user(user_id: int) -> BankingAccount:
    account_owner = user_service.get_user_by_id(user_id)
    if account_owner is None:
        return None
    result: BankingAccount = BankingAccount.objects.filter(account_owner=account_owner).first()
    return result
