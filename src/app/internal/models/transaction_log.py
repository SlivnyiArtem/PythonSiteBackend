from django.db import models

from app.internal.models.simple_user import SimpleUser


class TransactionLog(models.Model):
    # transaction_recipient_id = models.IntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=20, null=False)
    transaction_date = models.DateField(null=True)
    transaction_recipient = models.ForeignKey(SimpleUser, on_delete=models.SET_NULL)
    transaction_sender = models.ForeignKey(SimpleUser, on_delete=models.SET_NULL)
    # is_outgoing_transaction = models.BooleanField(null=False)
