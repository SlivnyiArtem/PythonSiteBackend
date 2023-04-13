# место для фикстур
import pytest

from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card
from app.internal.models.simple_user import SimpleUser


@pytest.fixture(scope="function")
def test_card_number():
    return 7777


@pytest.fixture(scope="function")
def test_acc_number():
    return 1


@pytest.fixture(scope="function")
def test_banking_account() -> BankingAccount:
    acc = BankingAccount.objects.create(account_number=7, account_owner=789, currency_amount=500)
    return acc


@pytest.fixture(scope="function")
def test_card() -> Card:
    simple_user_1 = SimpleUser.objects.create(user_id=256, full_username="grandfather")
    acc = BankingAccount.objects.create(account_number=3, account_owner=simple_user_1, currency_amount=500)
    card = Card.objects.create(card_number=7777, MM=5, YY=2020, system="VISA", banking_account=acc)
    return card


@pytest.fixture(scope="function")
def test_bank_acc():
    simple_user_1 = SimpleUser.objects.create(user_id=123, full_username="tzinch")
    acc = BankingAccount.objects.create(account_number=1, account_owner=simple_user_1, currency_amount=500)
    return acc