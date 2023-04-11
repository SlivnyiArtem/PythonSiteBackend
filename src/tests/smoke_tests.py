from unittest.mock import MagicMock

from django.test.client import Client
from rest_framework import status

import pytest

from internal.bot import Bot


# @pytest.mark.smoke
def test_start_bot():
    pass


@pytest.mark.smoke
def test_start_app():
    app_page = Client(enforce_csrf_checks=False).get("/admin/")
    assert app_page.status_code == status.HTTP_200_OK


# Запускается ли бот и не падает
# @pytest.fixture
# def test_start_bot():
#     bot = Bot()
#     mock_remove_webhook = MagicMock()
#     mock_run_webhooks = MagicMock()
#
#     monkeypatch.setattr(bot.application, "remove_webhook", mock_remove_webhook)
#     monkeypatch.setattr(bot.application, "run_webhooks", mock_run_webhooks)
#
#     bot.start()
#
#     assert mock_remove_webhook.called
#     assert mock_run_webhooks.called
