from ninja_extra import ControllerBase, api_controller, http_post
from ninja_extra.permissions import AllowAny
from ninja_jwt.controller import TokenVerificationController, schema


class CustomTokenObtainPairController(ControllerBase):
    auto_import = False

    @http_post(
        "/login",
        response=schema.obtain_pair_schema.get_response_schema(),
        url_name="login",
    )
    def obtain_token(self, user_token: schema.obtain_pair_schema):
        user_token.check_user_authentication_rule()
        return user_token.to_response_schema()

    @http_post(
        "/refresh",
        response=schema.obtain_pair_refresh_schema.get_response_schema(),
        url_name="token_refresh",
    )
    def refresh_token(self, refresh_token: schema.obtain_pair_refresh_schema):
        return refresh_token.to_response_schema()


@api_controller("/token", permissions=[AllowAny], tags=["token"])
class CustomController(TokenVerificationController, CustomTokenObtainPairController):
    auto_import = False
