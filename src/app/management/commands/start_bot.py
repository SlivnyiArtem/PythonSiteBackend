from app.internal import bot

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot.start_bot()
