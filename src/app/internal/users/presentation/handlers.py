from django.http import HttpResponse

from app.internal.models.transaction import Transaction
from app.internal.users.domain.services import UserService


class UserHandlers:
    def __init__(self, user_service: UserService):
        self._user_service = user_service

    def me_information(self, request):
        return self._user_service.get_me_information(request.user.username)

    def test_information(self):
        return self._user_service.get_test_information()

    # здесь функции
    def get_transactions_log(self, request):
        user_id = request.user.username
        user = self._user_service.get_user_by_id(user_id)

        sender_logs = list(Transaction.objects.filter(transaction_recipient=user))
        recipient_logs = list(Transaction.objects.filter(transaction_sender=user))

        new_sender = map(lambda sender: sender.full_username, sender_logs)
        new_recipient = map(lambda recipient: recipient.full_username, recipient_logs)
        res_dict = {"senders_log": new_sender, "recipient_logs": new_recipient}
        return HttpResponse(res_dict)
