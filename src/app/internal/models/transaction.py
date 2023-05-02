from django.db import models

from app.internal.models.simple_user import SimpleUser


class Transaction(models.Model):
    transaction_recipient = models.ForeignKey(
        SimpleUser, related_name="recipients", on_delete=models.SET_NULL, null=True
    )
    transaction_sender = models.ForeignKey(SimpleUser, related_name="senders", on_delete=models.SET_NULL, null=True)
    # transaction_recipient_id = models.IntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=20, null=False)
    transaction_date = models.DateField(null=True)
    # is_outgoing_transaction = models.BooleanField(null=False)
