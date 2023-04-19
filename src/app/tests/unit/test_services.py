from unittest.mock import MagicMock

import pytest

from app.internal.services.banking_service import get_acc_by_id, get_acc_by_user, get_card_by_id
from app.internal.services.user_service import get_user_by_id, get_user_by_username, update_user_number
from app.internal.transport.bot.handlers import transaction


@pytest.mark.django_db
def test_get_card_by_number_ok(test_card_1):
    card = get_card_by_id(test_card_1.card_number)
    assert card == test_card_1
    pass


@pytest.mark.django_db
def test_get_acc_by_acc_number_ok(test_bank_acc_1):
    acc = get_acc_by_id(test_bank_acc_1.account_number)
    assert acc == test_bank_acc_1


@pytest.mark.django_db
def test_get_acc_by_user_id_ok(test_bank_acc_1):
    acc = get_acc_by_user(123)
    assert acc == test_bank_acc_1


@pytest.mark.django_db
def test_get_user_username_ok(test_simple_user_for_handlers):
    user = get_user_by_username(test_simple_user_for_handlers.full_username)
    assert user == test_simple_user_for_handlers


@pytest.mark.django_db
def test_get_user_id_ok(test_simple_user_for_handlers):
    user = get_user_by_id(test_simple_user_for_handlers.user_id)
    assert user == test_simple_user_for_handlers


@pytest.mark.django_db
def test_update_user_telephone_ok(test_simple_user_for_handlers):
    user_start = test_simple_user_for_handlers
    update_user_number(test_simple_user_for_handlers.user_id, 79506372222)
    user = get_user_by_id(test_simple_user_for_handlers.user_id)
    assert user_start.phone_number == test_simple_user_for_handlers.phone_number
    assert user.phone_number == 79506372222


@pytest.mark.django_db
def test_transact_ok(test_bank_acc_1, test_bank_acc_2):
    bot = MagicMock()
    message = MagicMock()
    amount = 2
    amount_1 = test_bank_acc_1.currency_amount
    amount_2 = test_bank_acc_2.currency_amount
    transaction(bot, message, amount, test_bank_acc_1, test_bank_acc_2)
    assert amount_1 - test_bank_acc_1.currency_amount == amount
    assert test_bank_acc_2.currency_amount - amount_2 == amount
