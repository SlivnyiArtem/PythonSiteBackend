from unittest.mock import MagicMock

import environ
import pytest
import telebot
from django.test.client import Client
from rest_framework import status

env = environ.Env()
environ.Env.read_env()


@pytest.mark.smoke
def test_app_redirect_registration():
    app_page = Client(enforce_csrf_checks=False).get("/admin/")
    assert app_page.status_code == status.HTTP_302_FOUND


@pytest.mark.smoke
def test_app_start():
    app_page = Client(enforce_csrf_checks=False).get("/admin/login/?next=/admin/")
    assert app_page.status_code == status.HTTP_200_OK


@pytest.mark.smoke
def test_app_page():
    app_page = Client(enforce_csrf_checks=False).get("/testpage/")
    assert app_page.status_code == status.HTTP_200_OK


@pytest.mark.smoke
def test_bot_start():
    bot = telebot.TeleBot(env("BOT_KEY"))
    assert bot.get_me() is not None
