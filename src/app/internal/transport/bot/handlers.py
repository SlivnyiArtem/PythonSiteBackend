import phonenumbers
from app.internal.services import user_service
from app.internal.transport.bot.informing_handlers import dict_ser_to_str_ser
from app.internal.transport.information_former import form_information_handlers
from app.internal.transport.messages import common_messages


def currency_amount_handler(message, bot):
    msg = bot.send_message(message.chat.id,
                           common_messages.ask_for_card_acc_number())
    bot.register_next_step_handler(msg, get_amount, bot)


def get_amount(message, bot):
    user = form_information_handlers.try_get_user(message.from_user.id)
    if user is None:
        bot.send_message(message.chat.id,
                         common_messages.no_information_in_db_message)
    amount = form_information_handlers.\
        try_get_card_information(user, int(message.text))
    if amount is not None:
        bot.send_message(message.chat.id, amount)
    else:
        bot.send_message(message.chat.id,
                         common_messages.no_card_or_acc())


def help_handler(message, bot):
    bot.send_message(message.chat.id,
                     common_messages.help_command_message())


def me_inf_handler(message, bot):
    bot.send_message(message.chat.id,
                     dict_ser_to_str_ser
                     (form_information_handlers.
                      try_get_information(message.from_user.id)))


def start_handler(message, bot):
    user = message.from_user
    default_updates = {"name": user.first_name, "surname": user.last_name}
    user_service.update_create_user(user.id, default_updates)

    bot.send_message(message.chat.id, common_messages.
                     user_add_message(user.username))


def phone_number_handler(message, bot):
    msg = bot.send_message(message.chat.id,
                           common_messages.ask_for_phone_number_message())
    bot.register_next_step_handler(msg, get_phone_number, bot)


def get_phone_number(message, bot):
    if phonenumbers.is_valid_number(phonenumbers.parse(message.text, "IN")):
        number = int(message.text)

        user_service.update_user_number(message.from_user.id, number)

        bot.send_message(message.chat.id,
                         common_messages.
                         add_phone_number_message(message.from_user.username))
    else:
        msg = bot.send_message(message.chat.id,
                               common_messages.
                               incorrect_phone_number_message())
        bot.register_next_step_handler(msg, get_phone_number, bot)
