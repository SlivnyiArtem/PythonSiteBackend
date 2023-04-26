from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from app.internal.transport.rest import handlers

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.internal.urls")),
    path("testpage/", handlers.test_page),
    path("login/", handlers.LoginView.as_view()),
    path("users/<int:user_id>/me", handlers.me_http_inf_handler),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
