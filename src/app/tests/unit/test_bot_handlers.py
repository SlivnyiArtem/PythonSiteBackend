from unittest.mock import ANY, MagicMock

import pytest

from app.internal.services import banking_service
from app.internal.transport.bot import handlers
from app.internal.transport.bot.handlers import get_data_and_transact


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
    message = MagicMock()
    handlers.currency_amount_handler(message, test_mock_bot)
    handlers.currency_amount_handler.assert_called_once_with(message, test_mock_bot)


@pytest.mark.handler
def test_add_money_recipient(test_mock_bot, mocker):
    mocker.patch.object(handlers, "add_money_recipient")
    message = MagicMock()
    handlers.add_money_recipient(message, test_mock_bot)
    handlers.add_money_recipient.assert_called_once_with(message, test_mock_bot)


@pytest.mark.django_db
def test_transaction_by_username(mocker, test_bank_acc_2, test_card_1, test_bank_acc_1):
    mocker.patch.object(banking_service, "get_acc_by_user", return_value=MagicMock())
    mocker.patch.object(handlers, "transaction")
    message = MagicMock(text="7777 tzinch 100")
    bot = MagicMock()
    get_data_and_transact(message, bot, "1")
    handlers.transaction.assert_called_once_with(bot, message, test_bank_acc_1.account_number, test_bank_acc_1, ANY)


@pytest.mark.django_db
def test_transaction_by_card(mocker, test_bank_acc_2, test_card_1, test_bank_acc_1, test_card_2):
    mocker.patch.object(banking_service, "get_acc_by_id", return_value=MagicMock())
    mocker.patch.object(handlers, "transaction")
    message = MagicMock(text="7777 8888 100")
    bot = MagicMock()
    get_data_and_transact(message, bot, "2")
    handlers.transaction.assert_called_once_with(bot, message, test_bank_acc_1.account_number, test_bank_acc_1, ANY)


@pytest.mark.django_db
def test_transaction_by_bank_acc(mocker, test_card_1, test_bank_acc_1, test_bank_acc_2):
    mocker.patch.object(banking_service, "get_acc_by_id", return_value=MagicMock())
    mocker.patch.object(handlers, "transaction")
    message = MagicMock(text="7777 1 100")
    bot = MagicMock()
    get_data_and_transact(message, bot, "3")
    handlers.transaction.assert_called_once_with(bot, message, test_bank_acc_1.account_number, test_bank_acc_1, ANY)


@pytest.mark.handler
def test_transaction_incorrect_reqs(mocker):
    mocker.patch.object(banking_service, "get_card_by_id", return_value=MagicMock(banking_account=MagicMock()))
    mocker.patch.object(handlers, "transaction")
    chat = MagicMock(id=665)
    message = MagicMock(text="4 cgdfg 100", chat=chat)
    bot = MagicMock()
    get_data_and_transact(message, bot, "4")
    bot.send_message.assert_called_once_with(message.chat.id, "incorrect data")
