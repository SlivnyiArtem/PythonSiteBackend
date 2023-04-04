import phonenumbers

from app.internal.services import user_service
from app.internal.transport.bot.text_serialization_handlers import convert_dict_to_str
from app.internal.transport.information_former import form_information_handlers
from app.internal.transport.messages import common_messages


from telegram import ForceReply, Update
from telegram.ext import ContextTypes


def error_handler(exc, update: Update, context):
    update.message.reply_text(common_messages.MESSAGE_DICT.get("error_send_message") + f" {exc}")


def error_decorator(orig_func):
    def wrapper(*args, **kwargs):
        try:
            orig_func(*args, **kwargs)
        except Exception as exc:
            error_handler(exc, args[0], args[1])

    return wrapper


@error_decorator
def help_handler(update: Update, context):
    update.message.reply_text(common_messages.help_command_message())


# def error_handler(exc, message, bot):
#     bot.send_message(message.chat.id, common_messages.MESSAGE_DICT.get("error_send_message") + f" {exc}")
#
#
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
# def help_handler(message, bot):
#     bot.send_message(message.chat.id, common_messages.help_command_message())

# ----------------------------

# @error_decorator
# def currency_amount_handler(message, bot):
#     msg = bot.send_message(message.chat.id, common_messages.ask_for_card_acc_number())
#     bot.register_next_step_handler(msg, send_amount_inf, bot)
#
#
# def send_amount_inf(message, bot):
#     user = form_information_handlers.get_user_information(message.from_user.id)
#     if user is None:
#         bot.send_message(message.chat.id, common_messages.no_information_in_db_message)
#         return
#     try:
#         amount = form_information_handlers.get_currency_information(user, int(message.text))
#     except PermissionError:
#         bot.send_message(message.chat.id, common_messages.access_denied())
#         return
#     if amount is not None:
#         bot.send_message(message.chat.id, amount)
#     else:
#         bot.register_next_step_handler(
#             bot.send_message(message.chat.id, common_messages.no_card_or_acc()), send_amount_inf, bot
#         )


# @error_decorator
# def help_handler(message, bot):
#     bot.send_message(message.chat.id, common_messages.help_command_message())


# @error_decorator
# def me_inf_handler(message, bot):
#     bot.send_message(
#         message.chat.id, convert_dict_to_str(form_information_handlers.get_user_information(message.from_user.id))
#     )
#
#
# @error_decorator
# def start_handler(message, bot):
#     user = message.from_user
#     default_updates = {"name": user.first_name, "surname": user.last_name}
#     user_service.update_create_user(user.id, default_updates)
#
#     bot.send_message(message.chat.id, common_messages.user_add_message(user.username))
#
#
# @error_decorator
# def phone_number_handler(message, bot):
#     msg = bot.send_message(message.chat.id, common_messages.ask_for_phone_number_message())
#     bot.register_next_step_handler(msg, get_phone_number, bot)
#
#
# def get_phone_number(message, bot):
#     if phonenumbers.is_valid_number(phonenumbers.parse(message.text, "IN")):
#         number = int(message.text)
#
#         user_service.update_user_number(message.from_user.id, number)
#
#         bot.send_message(message.chat.id, common_messages.add_phone_number_message(message.from_user.username))
#     else:
#         msg = bot.send_message(message.chat.id, common_messages.incorrect_phone_number_message())
#         bot.register_next_step_handler(msg, get_phone_number, bot)
