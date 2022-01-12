
from telegram.ext import ApplicationBuilder, CommandHandler

from app.internal.transport.bot import handlers

class Bot:
    def __init__(self):
        self.application = ApplicationBuilder().token('6007627790:AAG3MqSDVIFkzfCRmYNDJNWc1UOqFpHxYdw').build()
        start_handler = CommandHandler('start', handlers.start_handler)
        self.application.add_handler(start_handler)
        # self.application.run_polling()

    def start(self):
        self.application.run_polling()


def start_bot():
    bot = Bot()
    bot.start()


if __name__ == '__main__':
    start_bot()
    # application = ApplicationBuilder().token('6007627790:AAG3MqSDVIFkzfCRmYNDJNWc1UOqFpHxYdw').build()
    # start_handler = CommandHandler('start',start)
    # application.add_handler(start_handler)
    # application.run_polling()
