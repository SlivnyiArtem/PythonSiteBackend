import decimal

import pytest

from app.internal.models.simple_user import SimpleUser
from app.internal.transport.bot import handlers
from app.internal.transport.messages import common_messages

# from internal.bot import Bot


@pytest.mark.django_db
def test_help_handler(test_mock_message, test_mock_bot):
    handlers.help_handler(test_mock_message, test_mock_bot)
    test_mock_bot.send_message.assert_called_once_with(
        test_mock_message.chat.id, common_messages.help_command_message()
    )


@pytest.mark.django_db
def test_me_handler(test_mock_message, test_mock_bot):
    handlers.start_handler(test_mock_message, test_mock_bot)
    handlers.me_inf_handler(test_mock_message, test_mock_bot)
    test_mock_bot.send_message.assert_called_with(
        test_mock_message.chat.id,
        "user_id : 112\n"
        "full_username : vortex2\n"
        "user_name : John\n"
        "surname : Doe\n"
        "phone_number : 79506376666\n"
        "friends : ['Krigg']\n",
    )


@pytest.mark.django_db
def test_currency_amount_handler_ok(
    test_mock_message_2, test_mock_bot, test_simple_user_for_handlers, test_simple_bank_acc_for_handlers
):
    # handlers.start_handler(test_mock_message_2, test_mock_bot)
    handlers.send_amount_inf(test_mock_message_2, test_mock_bot)
    test_mock_bot.send_message.assert_called_once_with(
        test_mock_message_2.chat.id, decimal.Decimal(test_simple_bank_acc_for_handlers.currency_amount)
    )


@pytest.mark.django_db
def test_start_handler(test_mock_message, test_mock_bot, test_simple_user_for_handlers):
    handlers.start_handler(test_mock_message, test_mock_bot)
    # print(test_simple_user_for_handlers.user_id)
    assert SimpleUser.objects.filter(user_id=test_simple_user_for_handlers.user_id).exists()


@pytest.mark.django_db
def test_add_fav_handler(test_new_friend_message, test_mock_bot, test_simple_user_for_handlers_2):
    # handlers.add_user(test_new_friend_message, test_mock_bot)
    # test_mock_bot.send_message.assert_called_once_with(test_new_friend_message.chat.id,
    #                                                    "Successful add user to money-friends")
    # assert test_simple_user_for_handlers_2.friends == ["Krigg", "Solanum"]
    pass


@pytest.mark.django_db
def test_remove_fav_handler():
    pass


@pytest.mark.django_db
def test_ls_fav_handler(test_mock_message, test_mock_bot):
    handlers.my_money_recipient(test_mock_message, test_mock_bot)
    test_mock_bot.send_message.assert_called_with(test_mock_message.chat.id, "Krigg\n")


@pytest.mark.django_db
def test_transaction_ok(test_mock_message, test_mock_bot, test_bank_acc, test_bank_acc_rec):
    # l = test_mock_message_ok.split()
    start_amount_1 = test_bank_acc.currency_amount
    start_amount_2 = test_bank_acc_rec.currency_amount
    # card = Card.objects.filter(card_number=l[0]).first()
    # test_bank_acc, test_bank_acc_rec = card.banking_account, l[1]
    handlers.transaction(test_mock_bot, test_mock_message, 5, test_bank_acc, test_bank_acc_rec)
    assert (
        test_bank_acc.currency_amount + 5 == start_amount_1 and test_bank_acc_rec.currency_amount - 5 == start_amount_2
    )
    test_mock_bot.send_message.assert_called_once_with(test_mock_message.chat.id, "transaction confirmed")


@pytest.mark.django_db
def test_not_enough_money_transaction(test_mock_message, test_mock_bot, test_bank_acc, test_bank_acc_rec):
    start_amount_1 = test_bank_acc.currency_amount
    start_amount_2 = test_bank_acc_rec.currency_amount
    handlers.transaction(test_mock_bot, test_mock_message, 1000, test_bank_acc, test_bank_acc_rec)
    assert test_bank_acc.currency_amount == start_amount_1 and test_bank_acc_rec.currency_amount == start_amount_2
    test_mock_bot.send_message.assert_called_once_with(
        test_mock_message.chat.id, "not enough money or incorrect amount. Transaction will be cancelled"
    )