from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from app.internal.bot import Bot

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.internal.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
