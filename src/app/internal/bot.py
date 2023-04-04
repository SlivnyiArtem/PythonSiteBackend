import environ
import telegram
from telegram.ext import CommandHandler, Updater

from app.internal.transport.bot import handlers

# import telebot


# from telegram import Bot as b


env = environ.Env()
environ.Env.read_env()


# class Bot:
#     def __init__(self):
#         self.application = telebot.TeleBot(env("BOT_KEY"))
#         self.application.message_handler(commands=["help"])(
#             lambda message: handlers.help_handler(message, self.application)
#         )
#         self.application.message_handler(commands=["start"])(
#             lambda message: handlers.start_handler(message, self.application)
#         )
#
#         self.application.message_handler(commands=["set_phone"])(
#             lambda message: handlers.phone_number_handler(message, self.application)
#         )
#
#         self.application.message_handler(commands=["me"])(
#             lambda message: handlers.me_inf_handler(message, self.application)
#         )
#
#         self.application.message_handler(commands=["check_currency"])(
#             lambda message: handlers.currency_amount_handler(message, self.application)
#         )
#
#     def start(self):
#         self.application.infinity_polling()
#
#
# def start_bot():
#     bot = Bot()
#     bot.start()


class Bot:
    def __init__(self):
        self.application = telegram.Bot(env("BOT_KEY"))
        self.updater = Updater(env("BOT_KEY"))
        self.dispatcher = self.updater.dispatcher
        self.dispatcher.add_handler(CommandHandler("help", handlers.help_handler))


def get_key():
    with open("/etc/letsencrypt/live/flamberg.backend23.2tapp.cc/cert.pem", "r") as f:
        print(f.read())
        return f.read()


def start_bot():
    bot = Bot()
    bot.updater.start_webhook(
        listen="127.0.0.1",
        port=5000,
        url_path=env("BOT_KEY"),
        cert=get_key(),
        # cert=open('/etc/letsencrypt/live/${MY_DOMEN}/cert.pem', 'rb'),
        # key="/etc/letsencrypt/live/${MY_DOMEN}/privkey.pem",
        # cert="/etc/letsencrypt/live/${MY_DOMEN}/fullchain.pem",
        webhook_url="${MY_DOMEN}/${BOT_KEY}",
    )
    bot.updater.idle()
    # bot.updater.start_polling()


if __name__ == "__main__":
    start_bot()
