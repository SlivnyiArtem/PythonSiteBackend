# url для модуля
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from app.internal.transport.rest import me_endpoint
from config.urls import api

urlpatterns = [
    # path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # path("admin/", admin.site.urls),
    path("api/", include("app.internal.urls")),
    path("/testo/", me_endpoint.testo),
    path("", api.urls),
    # path("userapi/<int:user_id>/newtestpage/", handlers.test_page_new),
    # path("login/", user_login_endpoint.UserLoginView.as_view()),
    # path("userapi/<int:user_id>/me", me_endpoint.me),
    # path('', include('rest_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
