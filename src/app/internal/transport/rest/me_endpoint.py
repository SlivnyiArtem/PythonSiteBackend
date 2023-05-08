from ninja import Router

rest_app_router = Router()


@rest_app_router.get("/test")
def test(request):
    return "TOK"


# from app.internal.transport.information_former import form_information_handlers
#
# api = NinjaExtraAPI()
# api.register_controllers(NinjaJWTDefaultController)
#
# router = ninja.Router()
#
#
# def me(request, user_id):
#     information = form_information_handlers.get_user_information(user_id)
#     return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
#
#
# class AuthBearer(HttpBearer):
#     async def authenticate(self, request, token):
#         return True
#
#
# @api_controller(auth=NOT_SET, permissions=[])
# class MyController:
#     @route.get("/me2", auth=JWTAuth())
#     async def me(self):
#         return HttpResponse("sdlkfj")
#         # user_id = self.request.auth.user_id
#         # information = form_information_handlers.get_user_information(user_id)
#         # return JsonResponse(information, json_dumps_params={"ensure_ascii": False}, status=information["error_code"])
