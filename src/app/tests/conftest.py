# место для фикстур
from unittest.mock import MagicMock

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
def transact_msg_1():
    message = MagicMock()
    message.text = "7777 2 5"
    return message


@pytest.fixture(scope="function")
def test_banking_account() -> BankingAccount:
    acc = BankingAccount.objects.get_or_create(account_number=7, account_owner=789, currency_amount=500)[0]
    return acc


@pytest.fixture(scope="function")
def test_card() -> Card:
    simple_user_1 = SimpleUser.objects.get_or_create(user_id=256, full_username="tzinch")[0]
    acc = BankingAccount.objects.get_or_create(account_number=56, account_owner=simple_user_1, currency_amount=500)[0]
    card = Card.objects.get_or_create(card_number=7777, MM=5, YY=2020, system="VISA", banking_account=acc)[0]
    return card

@pytest.fixture(scope="function")
def another_test_Card() -> Card:
    simple_user_1 = SimpleUser.objects.get_or_create(user_id=257, full_username="khorn")[0]
    acc = BankingAccount.objects.get_or_create(account_number=2, account_owner=simple_user_1, currency_amount=500)[0]
    card = Card.objects.get_or_create(card_number=8888, MM=5, YY=2020, system="VISA", banking_account=acc)[0]
    return card


@pytest.fixture(scope="function")
def test_bank_acc():
    simple_user_1 = SimpleUser.objects.get_or_create(user_id=123, full_username="tzinch")[0]
    acc = BankingAccount.objects.get_or_create(account_number=1, account_owner=simple_user_1, currency_amount=500)[0]
    return acc




@pytest.fixture(scope="function")
def test_mock_message():
    user = SimpleUser.objects.get_or_create(
        user_id=112,
        full_username="vortex2",
        user_name="John",
        surname="Doe",
        phone_number=79506376666,
        friends=["Krigg"],
    )[0]
    message = MagicMock()
    message.from_user = user
    message.from_user.id = 112
    return message
