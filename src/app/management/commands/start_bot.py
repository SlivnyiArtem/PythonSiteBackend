from django.core.management.base import BaseCommand, CommandError
from app.internal import bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot.start_bot()
