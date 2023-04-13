# from unittest.mock import MagicMock
# import pytest
# from app.internal.transport.bot import handlers
#
#
# @pytest.mark.handler
# def test_help_handler(test_mock_bot, mocker):
#     mocker.patch.object(handlers, 'help_handler')
#     message = MagicMock()
#     test_mock_bot.application.message_handlers.handlers[0](message)
#     handlers.help_handler.assert_called_once_with(message, test_mock_bot.application)
#
#
# def test_start_handler(test_mock_bot, mocker):
#     mocker.patch.object(handlers, 'start_handler')
#     message = MagicMock()
#     test_mock_bot.application.message_handlers.handlers[1](message)
#     handlers.start_handler.assert_called_once_with(message, test_mock_bot.application)
#
#
# def test_phone_number_handler(test_mock_bot, mocker):
#     mocker.patch.object(handlers, 'phone_number_handler')
#     message = MagicMock()
#     test_mock_bot.application.message_handlers.handlers[2](message)
#     handlers.phone_number_handler.assert_called_once_with(message, test_mock_bot.application)
#
#
# def test_me_inf_handler(test_mock_bot, mocker):
#     mocker.patch.object(handlers, 'me_inf_handler')
#     message = MagicMock()
#     test_mock_bot.application.message_handlers.handlers[3](message)
#     handlers.me_inf_handler.assert_called_once_with(message, test_mock_bot.application)
#
#
# def test_currency_amount_handler(test_mock_bot, mocker):
#     mocker.patch.object(handlers, 'currency_amount_handler')
#     message = MagicMock()
#     test_mock_bot.application.message_handlers.handlers[4](message)
#     handlers.currency_amount_handler.assert_called_once_with(message, test_mock_bot.application)
#
#
# def test_add_money_recipient(test_mock_bot, mocker):
#     mocker.patch.object(handlers, 'add_money_recipient')
#     message = MagicMock()
#     test_mock_bot.application.message_handlers.handlers[5](message)
#     handlers.add_money_recipient.assert_called_once_with(message, test_mock_bot.application)
#
#
# def test_delete_money_recipient(test_mock_bot, mocker):
#     mocker.patch.object(handlers, 'delete_money_recipient')
#     message = MagicMock()
#     test_mock_bot.application.message_handlers.handlers[6](message)
#     handlers.delete_money_recipient.assert_called_once_with(message, test_mock_bot.application)
#
#
# def test_make_transaction(test_mock_bot, mocker):
#     mocker.patch.object(handlers, 'make_transaction')
#     message = MagicMock()
#     test_mock_bot.application.message_handlers.handlers[7](message)
#     handlers.make_transaction.assert_called_once_with(message, test_mock_bot.application)
#
#
# def test_my_money_recipient(test_mock_bot, mocker):
#     mocker.patch.object(handlers, 'my_money_recipient')
#     message = MagicMock()
#     test_mock_bot.application.message_handlers.handlers[8](message)
#     handlers.my_money_recipient.assert_called_once_with(message, test_mock_bot.application)
