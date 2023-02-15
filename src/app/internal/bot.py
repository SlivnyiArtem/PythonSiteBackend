import telebot

from app.internal.transport.bot import handlers


class Bot:
    def __init__(self):
        self.application = telebot.TeleBot('6007627790:AAG3MqSDVIFkzfCRmYNDJNWc1UOqFpHxYdw')
        self.application.message_handler(commands=['start'])(lambda message:
                                                             handlers.start_handler(message, self.application))

        self.application.message_handler(commands=['set_phone'])(lambda message:
                                                                 handlers.phone_number_handler(message,
                                                                                               self.application))

        self.application.message_handler(commands=['me'])(lambda message:
                                                          handlers.me_inf_handler(message, self.application))

    def start(self):
        self.application.infinity_polling()


def start_bot():
    bot = Bot()
    bot.start()


if __name__ == '__main__':
    start_bot()
