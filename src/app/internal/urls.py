from app.internal.transport.rest import handlers
from django.urls import path

urlpatterns = [
    path("users/<int:user_id>/me", handlers.me_http_inf_handler),
]
