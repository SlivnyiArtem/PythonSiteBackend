import phonenumbers

from app.internal.services import user_service
from app.internal.transport.bot.text_serialization_handlers import convert_dict_to_str
from app.internal.transport.information_former import form_information_handlers
from app.internal.transport.messages import common_messages


# from telegram import ForceReply, Update
# from telegram.ext import ContextTypes

#
# def error_handler(exc, update: Update, context):
#     update.message.reply_text(common_messages.MESSAGE_DICT.get("error_send_message") + f" {exc}")


# def error_decorator(orig_func):
#     def wrapper(*args, **kwargs):
#         try:
#             orig_func(*args, **kwargs)
#         except Exception as exc:
#             error_handler(exc, args[0], args[1])
#
#     return wrapper
#
#
# @error_decorator
# def help_handler(update: Update, context):
#     update.message.reply_text(common_messages.help_command_message())


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
def help_handler(message, bot):
    bot.send_message(message.chat.id, common_messages.help_command_message())


# ----------------------------


@error_decorator
def currency_amount_handler(message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_card_acc_number())
    bot.register_next_step_handler(msg, send_amount_inf, bot)


def send_amount_inf(message, bot):
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
def me_inf_handler(message, bot):
    bot.send_message(
        message.chat.id, convert_dict_to_str(form_information_handlers.get_user_information(message.from_user.id))
    )


@error_decorator
def start_handler(message, bot):
    user = message.from_user
    default_updates = {"user_name": user.first_name, "surname": user.last_name}
    user_service.update_create_user(user.id, default_updates)

    bot.send_message(message.chat.id, common_messages.user_add_message(user.username))


@error_decorator
def phone_number_handler(message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_phone_number_message())
    bot.register_next_step_handler(msg, get_phone_number, bot)


def get_phone_number(message, bot):
    if phonenumbers.is_valid_number(phonenumbers.parse(message.text, "IN")):
        number = int(message.text)

        user_service.update_user_number(message.from_user.id, number)

        bot.send_message(message.chat.id, common_messages.add_phone_number_message(message.from_user.username))
    else:
        msg = bot.send_message(message.chat.id, common_messages.incorrect_phone_number_message())
        bot.register_next_step_handler(msg, get_phone_number, bot)


@error_decorator
def my_money_recipient(message, bot):
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
def add_money_recipient(message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_user_name())
    bot.register_next_step_handler(msg, add_user, bot)


def add_user(message, bot):
    if message.text[0] != "@" or len(message.text.split()) != 1:
        answer = bot.send_message(message.chat.id, common_messages.incorrect_user_name())
        bot.register_next_step_handler(answer, add_user, bot)
    else:
        user = user_service.get_user_by_id(message.from_user.id)
        if user is None:
            return
        user.friends.append(message.text)
        user.save()
        bot.send_message(message.chat.id, "Successful add user to money-friends")


@error_decorator
def delete_money_recipient(message, bot):
    msg = bot.send_message(message.chat.id, common_messages.ask_for_user_name())
    bot.register_next_step_handler(msg, remove_user, bot)


def remove_user(message, bot):
    if message.text[0] != "@" or len(message.text.split()) != 1:
        answer = bot.send_message(message.chat.id, common_messages.incorrect_user_name())
        bot.register_next_step_handler(answer, remove_user, bot)
    else:
        user = user_service.get_user_by_id(message.from_user.id)
        if user is None:
            return
        user.friends.remove(message.text)
        user.save()
        bot.send_message(message.chat.id, "Successful delete user from money-friends")


@error_decorator
def make_transaction(message, bot):
    msg = bot.send_message(message.chat.id, "enter the transfer way you choose: \n"
                                            "by @username: 1\n by card_number: 2\n"
                                            "by bank_acc number: 3")
    bot.register_next_step_handler(msg, transaction_handler, bot)


def username_transaction(message, bot):
    pass


def card_transaction(message, bot):
    pass


def bank_acc_transaction(message, bot):
    pass


def transaction_handler(message, bot):
    func_dict = {"1": username_transaction,
                 "2": card_transaction,
                 "3": bank_acc_transaction}
    if message.text in func_dict.keys():
        func_dict[message.text]()
        bot.send_message(message.chat.id, "transaction confirmed")
    else:
        bot.send_message(message.chat.id, "incorrect input")
