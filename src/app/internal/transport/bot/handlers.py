import threading

from asgiref.sync import sync_to_async
from telegram import Update
from telegram.ext import ContextTypes

from app.internal.models.simple_user import SimpleUser


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user.name)
    print("@@Start")
    create_user(update)


def create_user(update: Update):
    print(update.effective_user.id)
    sync_to_async(SimpleUser.objects.update_or_create(user_id=update.effective_user.id, name=update.effective_user.first_name, surname=update.effective_user.last_name, phone_number = None))
