import environ
import telebot

from app.internal.transport.bot import handlers

env = environ.Env()
environ.Env.read_env()


class Bot:
    def __init__(self):
        self.application = telebot.TeleBot(env("BOT_KEY"))
        self.application.message_handler(commands=["help"])(
            lambda message: handlers.help_handler(message, self.application)
        )
        self.application.message_handler(commands=["start"])(
            lambda message: handlers.start_handler(message, self.application)
        )

        self.application.message_handler(commands=["set_phone"])(
            lambda message: handlers.phone_number_handler(message, self.application)
        )

        self.application.message_handler(commands=["me"])(
            lambda message: handlers.me_inf_handler(message, self.application)
        )

        self.application.message_handler(commands=["check_currency"])(
            lambda message: handlers.currency_amount_handler(message, self.application)
        )

    def start(self):
        self.application.infinity_polling()


def start_bot():
    bot = Bot()
    bot.start()


if __name__ == "__main__":
    start_bot()
