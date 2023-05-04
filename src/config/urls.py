from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView

from app.internal.transport.rest import handlers, me_endpoint, user_login_endpoint

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("admin/", admin.site.urls),
    path("api/", include("app.internal.urls")),
    path("userapi/<int:user_id>/newtestpage/", handlers.test_page_new),
    path("login/", user_login_endpoint.UserLoginView.as_view()),
    path("userapi/me", me_endpoint.me),
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
