from unittest.mock import MagicMock

import pytest

from app.internal.models.banking_account import BankingAccount
from app.internal.models.simple_user import SimpleUser


@pytest.fixture(scope="function")
def test_bank_acc_1() -> BankingAccount:
    user = SimpleUser.objects.create(user_id=123, full_username="khorn")
    return BankingAccount.objects.create(account_number=100, account_owner=user, currency_amount=500)


@pytest.fixture(scope="function")
def test_bank_acc_2() -> BankingAccount:
    user = SimpleUser.objects.create(user_id=232, full_username="tzinch")
    acc = BankingAccount.objects.create(account_number=9, account_owner=user, currency_amount=500)

    return acc


@pytest.fixture(scope="function")
def test_simple_user_for_handlers() -> SimpleUser:
    user = SimpleUser.objects.create(
        user_id=112,
        full_username="vortex",
        user_name="John",
        surname="Doe",
        phone_number=79506376666,
        friends=["Krigg"],
    )
    return user


@pytest.fixture(scope="function")
def test_mock_bot():
    bot = MagicMock()
    return bot
