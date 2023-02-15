
from telegram.ext import ApplicationBuilder, CommandHandler

from app.internal.transport.bot import handlers

import telebot

from app.internal.models.simple_user import SimpleUser


class Bot:
    def __init__(self):
        self.application = telebot.TeleBot('6007627790:AAG3MqSDVIFkzfCRmYNDJNWc1UOqFpHxYdw')

        @self.application.message_handler(commands=['start'])
        def send_welcome(message):
            SimpleUser.objects.update_or_create(user_id = message.from_user.id, name = "message.from_user.name", surname = "message.from_user.name")
            # SimpleUser.objects.update_or_create(user_id=messagef.effective_user.id, name=update.effective_user.first_name,
            #                                     surname=update.effective_user.last_name)
            self.application.reply_to(message, """\
        Hi there, I am EchoBot.
        I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
        """)

        # self.application = ApplicationBuilder().token('6007627790:AAG3MqSDVIFkzfCRmYNDJNWc1UOqFpHxYdw').build()
        # start_handler = CommandHandler('start', handlers.start_handler)
        # self.application.add_handler(start_handler)
        # self.application.run_polling()

    def start(self):
        self.application.infinity_polling()
        # self.application.run_polling()


def start_bot():
    bot = Bot()
    bot.start()
    # bot = Bot()
    # bot.start()


if __name__ == '__main__':
    start_bot()
    # application = ApplicationBuilder().token('6007627790:AAG3MqSDVIFkzfCRmYNDJNWc1UOqFpHxYdw').build()
    # start_handler = CommandHandler('start',start)
    # application.add_handler(start_handler)
    # application.run_polling()
