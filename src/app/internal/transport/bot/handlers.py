import threading
import phonenumbers
from asgiref.sync import sync_to_async
from telegram import Update
from telegram.ext import ContextTypes

from app.internal.models.simple_user import SimpleUser


def me_inf_handler(message, bot):
    result: SimpleUser = SimpleUser.objects.filter(user_id=message.from_user.id).first()
    print(result)
    print("@ME")
    if result is None:
        bot.send_message(message.chat.id, "К сожалению, в базе данных о Вас нет информации. "
                                          "Попробуйте добавить себя в неё командой /start")
    else:
        bot.send_message(message.chat.id, result.string_deserialize())


def start_handler(message, bot):
    user = message.from_user
    print("@START")
    default_updates = {"name": user.first_name, "surname": user.last_name}
    SimpleUser.objects.update_or_create(user_id=user.id, defaults=default_updates)
    bot.send_message(message.chat.id, f'пользователь {user.username} успешно добавлен в базу данных, '
                                      f'либо данные о нём обновлены')

    # SimpleUser.objects.update_or_create(user_id=messagef.effective_user.id, name=update.effective_user.first_name,
    #                                     surname=update.effective_user.last_name)


#     bot.reply_to(message, """\
# Hi there, I am EchoBot.
# I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
# """)

#
# async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(update.effective_user.name)
#     print("@@Start")
#     create_user(update)
#
#
# def create_user(update: Update):
#     print(update.effective_user.id)
#     sync_to_async(SimpleUser.objects.update_or_create(user_id=update.effective_user.id, name=update.effective_user.first_name, surname=update.effective_user.last_name, phone_number = None))


# @sync_to_async
# def add_phone_number(phone_number_input, update: Update):
#     AppUser.objects.filter(user_id=update.effective_user.id).update(phone_number = phone_number_input)
#     # user.phone_number = phone_number_input
#     # user.save(update_fields=["phone_number"])
def phone_number_handler(message, bot):
    # user = message.from_user
    print("@USER_PHONE")
    msg = bot.send_message(message.chat.id, 'Укажите номер телефона, который вы хотите добавить в базу')
    bot.register_next_step_handler(msg, get_phone_number, bot)
    '''
    bot.send_message(message.chat.id,
                     f'Телефонный номер успешно добавлен к данным пользователя {message.from_user.username}')
    '''

    # phone_number = bot.register_next_step_handler(msg, get_phone_number)
    # print(phone_number)
    # if phone_number is None:
    #     repeat_number_msg = bot.send_message(message.chat.id,
    #                                          "Неправильное введенный "
    #                                          "формат номера, введине номер из "
    #                                          "одних цифр, начинающийся с 8 или +7")
    #
    #     bot.register_next_step_handler(repeat_number_msg, get_phone_number)
    # else:
    #     SimpleUser.objects.filter(user_id=message.from_user.id).update(phone_number=phone_number)
    # # await context.bot.send_message(chat_id=update.effective_chat.id, text="SendCom: SetPhone")


def get_phone_number(message, bot):
    print("***")
    print(message.text)
    print("***")
    # print(phonenumbers.is_valid_number(phonenumbers.parse(message.text, "IN")))
    # print("SSSSS")

    # print(number)
    if phonenumbers.is_valid_number(phonenumbers.parse(message.text, "IN")):
        number = int(message.text)
        print(number)
        # return int(number)
        SimpleUser.objects.filter(user_id=message.from_user.id).update(phone_number=number)
        bot.send_message(message.chat.id,
                         f'Телефонный номер успешно добавлен к данным пользователя {message.from_user.username}')
    else:
        # bot.
        # return None
        #
        msg = bot.send_message(message.chat.id,"Некорректный номер, проверьте правильность формата, затем введите ещё раз")
        bot.register_next_step_handler(msg,
            get_phone_number, bot)
    # bot.reply_to(message, """\
    # Hi there, I am EchoBot.
    # I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
    # """)
