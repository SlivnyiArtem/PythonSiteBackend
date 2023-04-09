from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card
from app.internal.services import user_service


def get_card_by_id(card_number: int) -> Card:
    result: Card = Card.objects.filter(card_number=card_number).first()
    return result


def get_acc_by_id(acc_number: int) -> BankingAccount:
    result: BankingAccount = BankingAccount.objects.filter(account_number=acc_number).first()
    return result


def get_acc_by_user(user_id: int) -> BankingAccount:
    result: BankingAccount = BankingAccount.objects.filter(account_owner=user_service.get_user_by_id(user_id)).first()
    return result
