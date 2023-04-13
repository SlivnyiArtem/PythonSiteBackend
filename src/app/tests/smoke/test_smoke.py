from unittest.mock import MagicMock

import pytest
from django.test.client import Client
from rest_framework import status


@pytest.mark.smoke
def test_start_app():
    app_page = Client(enforce_csrf_checks=False).get("/admin/")
    assert app_page.status_code == status.HTTP_302_FOUND  # СМ nginx file


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
