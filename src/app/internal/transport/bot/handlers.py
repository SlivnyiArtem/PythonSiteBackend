import threading

from asgiref.sync import sync_to_async
from telegram import Update
from telegram.ext import ContextTypes

from app.internal.models.simple_user import SimpleUser


def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user.name)
    print("@@1")
    task = threading.Thread(target=create_user, args=update)
    task.start()
    task.join()


def create_user(update: Update):
    SimpleUser.objects.create(user_id=update.effective_user.id, name=update.effective_user.first_name,
                                        surname=update.effective_user.last_name)
