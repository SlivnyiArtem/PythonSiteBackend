from unittest.mock import MagicMock

import pytest

from app.internal.models.banking_account import BankingAccount
from app.tests.conftest import test_simple_user_for_handlers


@pytest.fixture(scope="function")
def test_simple_bank_acc_with_user(test_simple_user_for_handlers) -> BankingAccount:
    acc = BankingAccount.objects.get_or_create(
        account_number=10, account_owner=test_simple_user_for_handlers, currency_amount="250"
    )[0]
    return acc


@pytest.fixture(scope="function")
def test_mock_get_currency_message():
    message = MagicMock()
    message.from_user = test_simple_user_for_handlers
    message.from_user.id = 112
    message.text = "10"
    return message
