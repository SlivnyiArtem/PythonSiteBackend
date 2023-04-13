# место для фикстур
from unittest.mock import MagicMock

import pytest

from app.internal.models.banking_account import BankingAccount
from app.internal.models.banking_card import Card
from app.internal.models.simple_user import SimpleUser


@pytest.fixture(scope="function")
def test_mock_bot():
    bot = MagicMock()
    return bot


@pytest.fixture(scope="function")
def test_bank_acc_rec() -> BankingAccount:
    simple_user_2 = SimpleUser.objects.create(user_id=223, full_username="nurgle")
    acc = BankingAccount.objects.create(account_number=2, account_owner=simple_user_2, currency_amount=0)
    return acc


@pytest.fixture(scope="function")
def test_bank_acc() -> BankingAccount:
    simple_user_1 = SimpleUser.objects.create(user_id=123, full_username="tzinch")
    acc = BankingAccount.objects.create(account_number=1, account_owner=simple_user_1, currency_amount=500)
    return acc


@pytest.fixture(scope="function")
def test_card() -> Card:
    simple_user_3 = SimpleUser.objects.create(user_id=323, full_username="khorn")
    acc = BankingAccount.objects.create(account_number=3, account_owner=simple_user_3, currency_amount=500)
    card = Card.objects.create(card_number=7777, MM=5, YY=2020, system="VISA", banking_account=acc)
    return card


@pytest.fixture(scope="function")
def test_simple_user() -> SimpleUser:
    user = SimpleUser.objects.create(user_id=789, full_username="bloodgod")
    return user
