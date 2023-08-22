from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController


# from app.internal.transport.rest.controllers import CustomController
# from app.internal.users.db_data.repositories import UserRepository
# from app.internal.users.domain.services import UserService
# from app.internal.users.presentation.handlers import UserHandlers
# from app.internal.users.presentation.routers import get_users_router


def get_api():
    api = NinjaExtraAPI()
    api.register_controllers(NinjaJWTDefaultController)
    return api

    # user_repo = UserRepository()
    # user_service = UserService(user_repo=user_repo)
    # user_handlers = UserHandlers(user_service=user_service)
    # api.register_controllers(CustomController)
    # router = get_users_router(user_handlers)
    # api.add_router("/users", router)
    #
    # return api, user_service


ninja_api = get_api()
