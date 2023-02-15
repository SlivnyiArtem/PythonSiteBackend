import threading

from asgiref.sync import sync_to_async
from telegram import Update
from telegram.ext import ContextTypes

from app.internal.models.simple_user import SimpleUser


def start_handler(message, bot):
    user = message.from_user
    print(user.first_name)
    default_updates = {"name": user.first_name, "surname": user.last_name}
    SimpleUser.objects.update_or_create(user_id=user.id, defaults=default_updates)
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
