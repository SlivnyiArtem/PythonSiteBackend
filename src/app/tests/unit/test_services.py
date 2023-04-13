from unittest.mock import MagicMock

import pytest

from app.internal.services.banking_service import get_acc_by_id, get_acc_by_user, get_card_by_id
from app.internal.services.user_service import get_user_by_id, get_user_by_username, update_user_number
from app.internal.transport.bot.handlers import transaction


@pytest.mark.django_db
def test_get_card_by_number_ok(test_card):
    card = get_card_by_id(7777)
    assert card == test_card
    pass


@pytest.mark.django_db
def test_get_acc_by_acc_number_ok(test_acc_number_p, test_bank_acc):
    acc = get_acc_by_id(test_acc_number_p)
    assert acc == test_bank_acc


@pytest.mark.django_db
def test_get_acc_by_user_id_ok(test_user_id_p, test_bank_acc):
    acc = get_acc_by_user(test_user_id_p)
    assert acc == test_bank_acc


@pytest.mark.django_db
def test_get_user_username_ok(test_simple_user):  # Все
    user = get_user_by_username("bloodgod")
    assert user == test_simple_user


@pytest.mark.django_db
def test_get_user_id_ok(test_simple_user):
    user = get_user_by_id(789)
    assert user == test_simple_user


@pytest.mark.django_db
def test_update_user_telephone_ok(test_simple_user):
    user_start = test_simple_user
    update_user_number(test_simple_user.user_id, 79506372222)
    user = get_user_by_id(test_simple_user.user_id)
    assert user_start.phone_number is None
    assert user.phone_number == 79506372222


@pytest.mark.django_db
def test_transact_ok(test_bank_acc, test_bank_acc_rec):
    bot = MagicMock()
    message = MagicMock()
    amount = 2
    amount_1 = test_bank_acc.currency_amount
    amount_2 = test_bank_acc_rec.currency_amount
    transaction(bot, message, amount, test_bank_acc, test_bank_acc_rec)
    assert amount_1 - test_bank_acc.currency_amount == amount
    assert test_bank_acc_rec.currency_amount - amount_2 == amount
