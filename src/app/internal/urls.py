from django.urls import path

from app.internal.transport.rest import handlers

urlpatterns = [
    path("users/<int:user_id>/me", handlers.me_http_inf_handler),
]
