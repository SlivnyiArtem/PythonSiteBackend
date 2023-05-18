from app.internal.users.domain.services import UserService


class UserHandlers:
    def __init__(self, user_service: UserService):
        self._user_service = user_service

    def me_information(self):
        return self._user_service.get_me_information()

    def test_information(self):
        return self._user_service.get_test_information()

    # здесь функции
