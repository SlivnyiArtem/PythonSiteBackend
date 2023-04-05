from django.template.defaulttags import url
from django.urls import include, path

from app.internal.bot import Updater
from app.internal.transport.rest import handlers

urlpatterns = [
    url(r"^", include("django_telegrambot.urls")),
    path("users/<int:user_id>/me", handlers.me_http_inf_handler),
    path("", Updater.as_view(), name="update"),
]
