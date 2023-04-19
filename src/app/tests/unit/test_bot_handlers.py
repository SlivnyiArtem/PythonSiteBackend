from unittest.mock import MagicMock, ANY

import pytest

from app.internal.transport.bot import handlers
from app.internal.services import banking_service, user_service
from app.internal.transport.bot.handlers import transaction, get_data_and_transact
from app.internal.models.banking_account import BankingAccount


@pytest.mark.handler
def test_help_handler(test_mock_bot, mocker):
    mocker.patch.object(handlers, "help_handler")
    message = MagicMock()
    handlers.help_handler(message, test_mock_bot)
    handlers.help_handler.assert_called_once_with(message, test_mock_bot)


@pytest.mark.handler
def test_start_handler(test_mock_bot, mocker):
    mocker.patch.object(handlers, "start_handler")
    message = MagicMock()
    handlers.start_handler(message, test_mock_bot)
    handlers.start_handler.assert_called_once_with(message, test_mock_bot)


@pytest.mark.handler
def test_set_phone_number_handler(test_mock_bot, mocker):
    mocker.patch.object(handlers, "phone_number_handler")
    message = MagicMock()
    handlers.phone_number_handler(message, test_mock_bot)
    handlers.phone_number_handler.assert_called_once_with(message, test_mock_bot)


@pytest.mark.handler
def test_me_inf_handler(test_mock_bot, mocker):
    mocker.patch.object(handlers, "me_inf_handler")
    message = MagicMock()
    handlers.me_inf_handler(message, test_mock_bot)
    handlers.me_inf_handler.assert_called_once_with(message, test_mock_bot)


@pytest.mark.handler
def test_currency_amount_handler(test_mock_bot, mocker):
    mocker.patch.object(handlers, "currency_amount_handler")
    # mocker.patch.object(handlers, "send_amount_inf")
    message = MagicMock()
    handlers.currency_amount_handler(message, test_mock_bot)
    # handlers.send_amount_inf(message, test_mock_bot)
    # handlers.send_amount_inf.assert_called_once_with(message, test_mock_bot)
    handlers.currency_amount_handler.assert_called_once_with(message, test_mock_bot)


@pytest.mark.handler
def test_add_money_recipient(test_mock_bot, mocker):
    mocker.patch.object(handlers, "add_money_recipient")
    message = MagicMock()
    handlers.add_money_recipient(message, test_mock_bot)
    handlers.add_money_recipient.assert_called_once_with(message, test_mock_bot)
#
@pytest.mark.django_db
def test_transaction_by_username(mocker, another_test_bank_acc, test_card, test_bank_acc):
    # mocker.patch.object(banking_service, 'get_card_by_id', return_value=MagicMock(banking_account=MagicMock()))
    # mocker.patch.object(user_service, 'get_user_by_username', return_value=MagicMock(user_id=1))
    mocker.patch.object(banking_service, 'get_acc_by_user', return_value=MagicMock())
    mocker.patch.object(handlers, 'transaction')
    message = MagicMock(text='7777 tzinch 100')
    bot = MagicMock()
    get_data_and_transact(message, bot, "1")
    # banking_service.get_card_by_id.assert_called_once_with(1)
    # user_service.get_user_by_username.assert_called_once_with('username')
    # banking_service.get_acc_by_user.assert_called_once_with(1)
    handlers.transaction.assert_called_once_with(bot, message, 100, test_bank_acc, ANY)
@pytest.mark.django_db
def test_transaction_by_card(mocker, another_test_bank_acc, test_card, test_bank_acc, another_test_card):
    # mocker.patch.object(banking_service, 'get_card_by_id', return_value=MagicMock(banking_account=MagicMock()))
    mocker.patch.object(banking_service, 'get_acc_by_id', return_value=MagicMock())
    mocker.patch.object(handlers, 'transaction')
    message = MagicMock(text='7777 8888 100')
    bot = MagicMock()
    get_data_and_transact(message, bot, "2")
    #banking_service.get_card_by_id.assert_called_with(123456)
    #banking_service.get_acc_by_id.assert_not_called()
    handlers.transaction.assert_called_once_with(bot, message, 100, another_test_bank_acc, ANY)

@pytest.mark.django_db
def test_transaction_by_bank_acc(mocker, test_card, test_bank_acc, another_test_bank_acc):
    mocker.patch.object(banking_service, 'get_acc_by_id', return_value=MagicMock())
    mocker.patch.object(handlers, 'transaction')
    message = MagicMock(text='7777 1 100')
    bot = MagicMock()
    get_data_and_transact(message, bot, '3')
    # banking_service.get_acc_by_id.assert_called_once_with(123456)
    handlers.transaction.assert_called_once_with(bot, message, 100,
                                                 another_test_bank_acc, ANY)

def test_case_4(mocker):
    mocker.patch.object(banking_service, 'get_card_by_id', return_value=MagicMock(banking_account=MagicMock()))
    mocker.patch.object(handlers, 'transaction')
    message = MagicMock(text='4 100')
    bot = MagicMock()
    get_data_and_transact(message, bot, "4")
    # banking_service.get_card_by_id.assert_not_called()
    handlers.transaction.assert_called_once_with(bot, message, 100, MagicMock(), MagicMock())
