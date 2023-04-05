from os.path import join

import environ
import telebot
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from telebot import TeleBot, types

from app.internal.transport.bot import handlers

env = environ.Env()
environ.Env.read_env()


@csrf_exempt
class Bot:
    def __init__(self):
        self.application = TeleBot(env("BOT_KEY"))
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

    # @csrf_exempt
    # def start(self):
    #     print("hook")
    #     self.application.run_webhooks(
    #         webhook_url="https://" + env("MY_DOMEN") + "/bot/",
    #         url_path="bot",
    #         listen="0.0.0.0",
    #         port=127,
    #     )

    def start(self):
        print("straight")
        self.application.remove_webhook()
        # self.application.set_webhook(
        #     url="https://" + env("MY_DOMEN") + "/" + env("BOT_KEY"),
        #     # certificate=open("/etc/letsencrypt/live/" + env("MY_DOMEN") + "/fullchain.pem"),
        # )
        self.application.infinity_polling()


if __name__ == "__main__":
    bot = Bot()
    bot.start()
