import phonenumbers
import telebot

from app.internal.models.banking_account import BankingAccount
from app.internal.services import banking_service, user_service
from app.internal.transport.bot.text_serialization_handlers import convert_dict_to_str
from app.internal.transport.information_former import form_information_handlers
from app.internal.transport.messages import common_messages


def error_handler(exc, message, bot):
    bot.send_message(message.chat.id, common_messages.MESSAGE_DICT.get("error_send_message") + f" {exc}")


def error_decorator(orig_func):
    def wrapper(*args, **kwargs):
        try:
            orig_func(*args, **kwargs)
        except Exception as exc:
            error_handler(exc, args[0], args[1])

    return wrapper


@error_decorator
def help_handler(message: telebot.types.Message, bot):
    bot.send_message(message.chat.id, common_messages.help_command_message())


@error_decorator
def currency_amount_handler(message: telebot.types.Message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_card_acc_number())
    bot.register_next_step_handler(msg, send_amount_inf, bot)


def send_amount_inf(message: telebot.types.Message, bot):
    user_inf = form_information_handlers.get_user_information(message.from_user.id)
    if user_inf is None:
        bot.send_message(message.chat.id, common_messages.no_information_in_db_message)
        return
    try:
        amount = form_information_handlers.get_currency_information(user_inf, int(message.text))
    except PermissionError:
        bot.send_message(message.chat.id, common_messages.access_denied())
        return
    if amount is not None:
        bot.send_message(message.chat.id, amount)
    else:
        bot.register_next_step_handler(
            bot.send_message(message.chat.id, common_messages.no_card_or_acc()), send_amount_inf, bot
        )


@error_decorator
def me_inf_handler(message: telebot.types.Message, bot):
    bot.send_message(
        message.chat.id, convert_dict_to_str(form_information_handlers.get_user_information(message.from_user.id))
    )


@error_decorator
def start_handler(message: telebot.types.Message, bot):
    user = message.from_user
    default_updates = {"user_name": user.first_name, "surname": user.last_name, "full_username": user.username}
    user_service.update_create_user(user.id, default_updates)

    bot.send_message(message.chat.id, common_messages.user_add_message(user.username))


@error_decorator
def phone_number_handler(message: telebot.types.Message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_phone_number_message())
    bot.register_next_step_handler(msg, get_phone_number, bot)


def get_phone_number(message: telebot.types.Message, bot):
    if phonenumbers.is_valid_number(phonenumbers.parse(message.text, "IN")):
        number = int(message.text)
        user_service.update_user_number(message.from_user.id, number)
        bot.send_message(message.chat.id, common_messages.add_phone_number_message(message.from_user.username))
    else:
        msg = bot.send_message(message.chat.id, common_messages.incorrect_phone_number_message())
        bot.register_next_step_handler(msg, get_phone_number, bot)


@error_decorator
def my_money_recipient(message: telebot.types.Message, bot):
    user = user_service.get_user_by_id(message.from_user.id)
    if user is None:
        bot.send_message(message.chat.id, common_messages.no_information_in_db_message)
        return
    spec_users = user.friends
    if len(spec_users) == 0:
        bot.send_message(message.chat.id, "No users in money-friends_list")
        return
    msg = ""
    for user in spec_users:
        msg += user + "\n"
    bot.send_message(message.chat.id, "This is your money-friends list:")
    bot.send_message(message.chat.id, msg)


@error_decorator
def add_money_recipient(message: telebot.types.Message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_user_name())
    bot.register_next_step_handler(msg, add_user, bot)


def add_user(message: telebot.types.Message, bot):
    if message.text[0] != "@" or len(message.text.split()) != 1:
        answer = bot.send_message(message.chat.id, common_messages.incorrect_user_name())
        bot.register_next_step_handler(answer, add_user, bot)
    else:
        user = user_service.get_user_by_id(message.from_user.id)
        if user is None:
            return
        user.friends.append(message.text[1:])
        user.save()
        bot.send_message(message.chat.id, "Successful add user to money-friends")


@error_decorator
def delete_money_recipient(message: telebot.types.Message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_user_name())
    bot.register_next_step_handler(msg, remove_user, bot)


def remove_user(message: telebot.types.Message, bot):
    if message.text[0] != "@" or len(message.text.split()) != 1:
        answer = bot.send_message(message.chat.id, common_messages.incorrect_user_name())
        bot.register_next_step_handler(answer, remove_user, bot)
    else:
        user = user_service.get_user_by_id(message.from_user.id)
        if user is None:
            return
        user.friends.remove(message.text[1:])
        user.save()
        bot.send_message(message.chat.id, "Successful delete user from money-friends")


@error_decorator
def make_transaction(message: telebot.types.Message, bot):
    msg = bot.send_message(
        message.chat.id,
        "enter the transfer way you choose: \n" "by username: 1\n by card_number: 2\n" "by bank_acc number: 3",
    )
    bot.register_next_step_handler(msg, ask_for_requisites, bot)


def ask_for_requisites(message: telebot.types.Message, bot):
    msg = bot.send_message(
        message.chat.id,
        "enter your card number, then card number/bank acc/ username of another user and amount of money to transfer",
    )
    func_dict = {"1": "username_transaction", "2": "card_transaction", "3": "bank_acc_transaction"}
    if message.text in func_dict.keys():
        bot.register_next_step_handler(msg, get_data_and_transact, bot, message.text)
        # bot.register_next_step_handlers(msg, lambda l: t(message.text, ), bot)
        # bot.register_next_step_handler(msg, func_dict[message.text], bot)
    else:
        bot.send_message(message.chat.id, "incorrect input")


def transaction(
    bot, message: telebot.types.Message, amount: int, bank_acc: BankingAccount, another_bank_acc: BankingAccount
):
    if send_msg_if_not_enough_money(bot, message.chat.id, amount, bank_acc.currency_amount):
        return
    bank_acc.currency_amount -= amount
    bank_acc.save()
    another_bank_acc.currency_amount += amount
    another_bank_acc.save()
    confirm_transaction(bot, message.chat.id)


def get_data_and_transact(message: telebot.types.Message, bot, text: str):
    reqs = message.text.split()
    amount = int(reqs[2])
    bank_acc = banking_service.get_card_by_id(int(reqs[0])).banking_account
    if text == "1":
        another_user_name = reqs[1]
        another_user = user_service.get_user_by_username(another_user_name)
        another_bank_acc = banking_service.get_acc_by_user(another_user.user_id)
    elif text == "2":
        another_card_number = int(reqs[1])
        another_card = banking_service.get_card_by_id(another_card_number)
        another_bank_acc = another_card.banking_account
    elif text == "3":
        another_bank_acc_number = int(reqs[1])
        another_bank_acc = banking_service.get_acc_by_id(another_bank_acc_number)
    else:
        another_bank_acc = bank_acc

    transaction(bot, message, amount, bank_acc, another_bank_acc)


# def username_transaction(message: telebot.types.Message, bot):
#     reqs = message.text.split()
#     our_card_number, another_user_name, amount = reqs[0], reqs[1], int(reqs[2])
#     card = banking_service.get_card_by_id(int(our_card_number))
#     bank_acc = card.banking_account
#
#     another_user = user_service.get_user_by_username(another_user_name)
#     another_bank_acc = banking_service.get_acc_by_user(another_user.user_id)
#     transaction(bot, message, amount, bank_acc, another_bank_acc)
#
#
# def card_transaction(message: telebot.types.Message, bot):
#     reqs = message.text.split()
#     our_card_number, another_card_number, amount = int(reqs[0]), int(reqs[1]), int(reqs[2])
#     card = banking_service.get_card_by_id(our_card_number)
#     another_card = banking_service.get_card_by_id(another_card_number)
#     bank_acc = card.banking_account
#     another_bank_acc = another_card.banking_account
#     transaction(bot, message, amount, bank_acc, another_bank_acc)
#
#
# def bank_acc_transaction(message: telebot.types.Message, bot):
#     reqs = message.text.split()
#     our_card_number, another_bank_acc_number, amount = int(reqs[0]), int(reqs[1]), int(reqs[2])
#     another_bank_acc = banking_service.get_acc_by_id(another_bank_acc_number)
#     card = banking_service.get_card_by_id(our_card_number)
#     bank_acc = card.banking_account
#     transaction(bot, message, amount, bank_acc, another_bank_acc)


def incorrect_reqs(user_cart: str, main_req: str, amount: str):
    return user_cart.isdigit() and main_req.isdigit() and amount.isdigit()


def send_msg_if_not_enough_money(bot, msg_id, transaction_amount, acc_amount):
    if transaction_amount <= 0 or acc_amount - transaction_amount < 0:
        bot.send_message(msg_id, "not enough money or incorrect amount. Transaction will be cancelled")
        return True
    return False


def confirm_transaction(bot, msg_id):
    bot.send_message(msg_id, "transaction confirmed")
