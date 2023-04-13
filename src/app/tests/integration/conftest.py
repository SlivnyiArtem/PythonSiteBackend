from decimal import Decimal
from unittest.mock import MagicMock

import pytest

from app.internal.models.banking_account import BankingAccount
from app.internal.models.simple_user import SimpleUser


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
def test_mock_message():
    user = SimpleUser.objects.create(
        user_id=112,
        full_username="vortex2",
        user_name="John",
        surname="Doe",
        phone_number=79506376666,
        friends=["Krigg"],
    )
    message = MagicMock()
    message.from_user = user
    message.from_user.id = 112
    return message


@pytest.fixture(scope="function")
def test_new_friend_message():
    user = SimpleUser.objects.create(
        user_id=112,
        full_username="vortex",
        user_name="John",
        surname="Doe",
        phone_number=79506376666,
        friends=["Krigg"],
    )
    message = MagicMock()
    message.from_user = user
    message.from_user.id = 112
    message.text = "@Solanum"
    return message


@pytest.fixture(scope="function")
def transact_msg_ok():
    message = MagicMock()
    message.text = "1111 2 5"
    return message


@pytest.fixture(scope="function")
def test_mock_bot():
    bot = MagicMock()
    return bot


@pytest.fixture(scope="function")
def test_simple_user_for_handlers_2() -> SimpleUser:
    user = SimpleUser.objects.get(
        user_id=112,
        full_username="vortex",
        user_name="John",
        surname="Doe",
        phone_number=79506376666,
        friends=["Krigg"],
    )
    return user


@pytest.fixture(scope="function")
def test_simple_user_for_handlers() -> SimpleUser:
    user = SimpleUser.objects.create(
        user_id=111,
        full_username="vortex",
        user_name="John",
        surname="Doe",
        phone_number=79506375555,
        friends=["Krigg"],
    )
    return user


@pytest.fixture(scope="function")
def test_simple_bank_acc_for_handlers() -> BankingAccount:
    user = SimpleUser.objects.filter(
        user_id=115,
        full_username="vortex",
        user_name="John",
        surname="Doe",
        phone_number=79506375555,
        friends=["Krigg"],
    ).first()
    acc = BankingAccount.objects.create(account_number=1, account_owner=user, currency_amount="25")
    return acc


@pytest.fixture(scope="function")
def test_simple_bank_acc_for_handlers_2() -> BankingAccount:
    user = SimpleUser.objects.filter(user_id=115, full_username="Krigg", friends=["vortex"]).first()
    acc = BankingAccount.objects.create(account_number=1, account_owner=user, currency_amount="0")
    return acc


@pytest.fixture(scope="function")
def test_mock_message_2():
    user = SimpleUser.objects.create(
        user_id=115,
        full_username="vortex",
        user_name="John",
        surname="Doe",
        phone_number=79506375555,
        friends=["Krigg"],
    )
    message = MagicMock()
    message.from_user = user
    message.from_user.id = 115
    return message
