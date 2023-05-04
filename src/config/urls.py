from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from app.internal.transport.rest import handlers, me_endpoint, user_login_endpoint

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.internal.urls")),
    path("userapi/<int:user_id>/newtestpage/", handlers.test_page_new),
    path("login/", user_login_endpoint.UserLoginView.as_view()),
    path("userapi/<int:user_id>/me", me_endpoint.MeInfView.as_view()),
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
