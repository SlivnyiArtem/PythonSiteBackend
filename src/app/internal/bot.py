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

        self.application.message_handler(commands=["add_money_recipient"])(
            lambda message: handlers.add_money_recipient(message, self.application)
        )

        self.application.message_handler(commands=["delete_money_recipient"])(
            lambda message: handlers.delete_money_recipient(message, self.application)
        )

        self.application.message_handler(commands=["make_transaction"])(
            lambda message: handlers.make_transaction(message, self.application)
        )

        self.application.message_handler(commands=["my_money_recipient"])(
            lambda message: handlers.my_money_recipient(message, self.application)
        )

        self.application.message_handler(commands=["get_full_log"])(
            lambda message: handlers.get_full_log(message, self.application)
        )

        self.application.message_handler(commands=["all_transaction_recipients"])(
            lambda message: handlers.all_transaction_recipients(message, self.application)
        )

        self.application.message_handler(commands=["new_password"])(
            lambda message: handlers.password_handler(message, self.application)
        )

    def start(self):
        self.application.remove_webhook()
        self.application.run_webhooks(
            listen="0.0.0.0", port=5000, webhook_url="https://" + env("MY_DOMEN") + "/bot", url_path="bot"
        )


if __name__ == "__main__":
    bot = Bot()
    bot.start()
