import phonenumbers
from app.internal.services import user_service
from app.internal.services.user_service import dict_ser_to_str_ser


def me_inf_handler(message, bot):
    bot.send_message(message.chat.id,
                     dict_ser_to_str_ser(user_service.try_get_information(message.from_user.id)))


def start_handler(message, bot):
    user = message.from_user
    default_updates = {"name": user.first_name, "surname": user.last_name}
    user_service.update_create_user(user.id, default_updates)

    bot.send_message(message.chat.id, f'пользователь {user.username} успешно добавлен в базу данных, '
                                      f'либо данные о нём обновлены')


def phone_number_handler(message, bot):
    msg = bot.send_message(message.chat.id, 'Укажите номер телефона, который вы хотите добавить в базу')
    bot.register_next_step_handler(msg, get_phone_number, bot)


def get_phone_number(message, bot):
    if phonenumbers.is_valid_number(phonenumbers.parse(message.text, "IN")):
        number = int(message.text)

        user_service.update_user_number(message.from_user.id, number)

        bot.send_message(message.chat.id,
                         f'Телефонный номер успешно добавлен к данным пользователя {message.from_user.username}')
    else:
        msg = bot.send_message(message.chat.id,
                               "Некорректный номер, проверьте правильность формата, затем введите ещё раз")
        bot.register_next_step_handler(msg,
                                       get_phone_number, bot)
