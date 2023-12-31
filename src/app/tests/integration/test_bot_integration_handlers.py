# import decimal
#
# import pytest
#
# from app.internal.users.db_data.models import SimpleUser
# from app.internal.transport.bot import handlers
# from app.internal.transport.messages import common_messages
#
#
# @pytest.mark.django_db
# def test_help_handler(test_mock_message, test_mock_bot):
#     handlers.help_handler(test_mock_message, test_mock_bot)
#     test_mock_bot.send_message.assert_called_once_with(
#         test_mock_message.chat.id, common_messages.help_command_message()
#     )
#
#
# @pytest.mark.django_db
# def test_me_handler(test_mock_message, test_mock_bot):
#     handlers.start_handler(test_mock_message, test_mock_bot)
#     handlers.me_inf_handler(test_mock_message, test_mock_bot)
#     test_mock_bot.send_message.assert_called_with(
#         test_mock_message.chat.id,
#         "user_id : 112\n"
#         "full_username : vortex\n"
#         "user_name : John\n"
#         "surname : Doe\n"
#         "phone_number : 79506376666\n"
#         "hash_of_password : None\n"
#         "login_access : True\n"
#         "friends : ['Rogue']\n",
#     )
#
#
# @pytest.mark.django_db
# def test_currency_amount_handler_ok(
#     test_mock_get_currency_message, test_mock_bot, test_simple_user_for_handlers, test_simple_bank_acc_with_user
# ):
#     handlers.send_amount_inf(test_mock_get_currency_message, test_mock_bot)
#     test_mock_bot.send_message.assert_called_once_with(
#         test_mock_get_currency_message.chat.id, decimal.Decimal(test_simple_bank_acc_with_user.currency_amount)
#     )
#
#
# @pytest.mark.django_db
# def test_start_handler(test_mock_message, test_mock_bot, test_simple_user_for_handlers):
#     handlers.start_handler(test_mock_message, test_mock_bot)
#     assert SimpleUser.objects.filter(user_id=test_simple_user_for_handlers.user_id).exists()
#
#
# @pytest.mark.django_db
# def test_add_fav_handler(
#     test_simple_user_for_handlers_0,
#     test_mock_message,
#     test_mock_bot,
#     test_simple_user_for_handlers,
#     test_simple_user_for_handlers_2,
# ):
#     handlers.add_user(test_mock_message, test_mock_bot)
#     test_mock_bot.send_message.assert_called_once_with(
#         test_mock_message.chat.id, "Successful add user to money-friends"
#     )
#     user = SimpleUser.objects.filter(user_id=test_simple_user_for_handlers.user_id).first()
#     # assert user.friends.all() == ["Krigg", "Solanum"]
#     assert list(user.friends.all()) == [test_simple_user_for_handlers_0, test_simple_user_for_handlers_2]
#
#
# @pytest.mark.django_db
# def test_show_fav_handler(test_mock_message, test_mock_bot, test_simple_user_for_handlers_0):
#     handlers.my_money_recipient(test_mock_message, test_mock_bot)
#     test_mock_bot.send_message.assert_called_with(
#         test_mock_message.chat.id, f"{test_simple_user_for_handlers_0.full_username}\n"
#     )
#
#
# @pytest.mark.django_db
# def test_transaction_ok(test_mock_message, test_mock_bot, test_bank_acc_1, test_bank_acc_2):
#     start_amount_1 = test_bank_acc_1.currency_amount
#     start_amount_2 = test_bank_acc_2.currency_amount
#     handlers.transaction(test_mock_bot, test_mock_message, 5, test_bank_acc_1, test_bank_acc_2)
#     assert (
#         test_bank_acc_1.currency_amount + 5 == start_amount_1 and test_bank_acc_2.currency_amount - 5 == start_amount_2
#     )
#     test_mock_bot.send_message.assert_called_once_with(test_mock_message.chat.id, "transaction confirmed")
#
#
# @pytest.mark.django_db
# def test_not_enough_money_transaction(test_mock_message, test_mock_bot, test_bank_acc_1, test_bank_acc_2):
#     start_amount_1 = test_bank_acc_1.currency_amount
#     start_amount_2 = test_bank_acc_2.currency_amount
#     handlers.transaction(test_mock_bot, test_mock_message, 1000, test_bank_acc_1, test_bank_acc_2)
#     assert test_bank_acc_1.currency_amount == start_amount_1 and test_bank_acc_2.currency_amount == start_amount_2
#     test_mock_bot.send_message.assert_called_once_with(
#         test_mock_message.chat.id, "not enough money or incorrect amount. Transaction will be cancelled"
#     )
