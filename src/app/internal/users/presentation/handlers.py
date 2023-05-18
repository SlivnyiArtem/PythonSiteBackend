from django.http import HttpResponse

from app.internal.models.transaction import Transaction
from app.internal.users.domain.services import UserService
from app.internal.users.presentation.entities import UserSchema


class UserHandlers:
    def __init__(self, user_service: UserService):
        self._user_service = user_service

    def me_information(self, request):
        return self._user_service.get_me_information(request.user.username)

    def test_information(self):
        return self._user_service.get_test_information()

    # здесь функции
    def get_transactions_log(self, request):
        username = request.user.username
        if username == "Admin":
            pass
        else:
            user_id = int(username)
            user = self._user_service.get_user_by_id(user_id)

            sender_logs = list(Transaction.objects.filter(transaction_recipient=user))
            recipient_logs = list(Transaction.objects.filter(transaction_sender=user))

            new_sender = map(lambda sender: sender.full_username, sender_logs)
            new_recipient = map(lambda recipient: recipient.full_username, recipient_logs)
            res_dict = {"senders_log": new_sender, "recipient_logs": new_recipient}
            return HttpResponse(res_dict)

    def create_user(self, user_schema: UserSchema):
        username = user_schema.user.username
        if username == "Admin":
            # user = self._user_service.get_user_by_id(user_id=username)

            password = "123"
            default_updates = {
                "user_name": user_schema["user_first_name"],
                "surname": user_schema["user_last_name"],
                "full_username": user_schema["user_full_username"],
            }
            auth_user = self._user_service.create_auth_user(user_schema["user_id"], password)
            return self._user_service.update_create_user(user_schema["user_id"], default_updates, auth_user)
        else:
            return

    def delete_user(self, user_schema: UserSchema):
        username = user_schema.user.username
        if username == "Admin":
            return self._user_service.delete_user(user_schema["user_id"])
        else:
            return
