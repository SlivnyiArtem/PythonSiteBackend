from ninja_extra import NinjaExtraAPI

from app.internal.transport.rest.Controllers import CustomController
from app.internal.users.db_data.repositories import UserRepository
from app.internal.users.domain.services import UserService
from app.internal.users.presentation.handlers import UserHandlers
from app.internal.users.presentation.routers import get_users_router


def get_api():
    api = NinjaExtraAPI()
    user_repo = UserRepository()
    user_service = UserService(user_repo=user_repo)
    # user_handlers = UserHandlers(user_service=user_service)
    api.register_controllers(CustomController)
    api.add_router("/users", get_users_router(UserHandlers(user_service=user_service)))  # !!!

    # add_users_router(api, user_handlers)

    return api, user_service


ninja_api, user_service = get_api()
