from django.template.defaulttags import url
from django.urls import include, path

from app.internal.transport.rest import handlers

urlpatterns = [
    path("users/<int:user_id>/me", handlers.me_http_inf_handler),
]
