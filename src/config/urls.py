from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView

from app.internal.transport.rest import handlers, me_endpoint, user_login_endpoint

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("admin/", admin.site.urls),
    path("api/", include("app.internal.urls")),
    path("userapi/<int:user_id>/newtestpage/", handlers.test_page_new),
    path("login/", user_login_endpoint.UserLoginView.as_view()),
    path("userapi/<int:user_id>/me", me_endpoint.me),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
