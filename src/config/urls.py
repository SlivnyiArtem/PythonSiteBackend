from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from app.internal.transport.rest import me_endpoint
from app.internal.transport.rest.me_endpoint import rest_app_router

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
#
api.add_router("/", rest_app_router)

urlpatterns = [
    # path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("admin/", admin.site.urls),
    path("api/", include("app.internal.urls")),
    path("testo/", me_endpoint.testo),
    path("", api.urls),
    # path("userapi/<int:user_id>/newtestpage/", handlers.test_page_new),
    # path("login/", user_login_endpoint.UserLoginView.as_view()),
    # path("userapi/<int:user_id>/me", me_endpoint.me),
    # path('', include('rest_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     # path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
#     path("admin/", admin.site.urls),
#     path("api/", include("app.internal.urls")),
#     path("/testo/", me_endpoint.testo),
#     path("", api.urls),
#     # path("userapi/<int:user_id>/newtestpage/", handlers.test_page_new),
#     # path("login/", user_login_endpoint.UserLoginView.as_view()),
#     # path("userapi/<int:user_id>/me", me_endpoint.me),
#     # path('', include('rest_urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
