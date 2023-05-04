from django.db import models

from app.internal.models.simple_user import SimpleUser


class Transaction(models.Model):
    transaction_recipient = models.ForeignKey(
        SimpleUser, related_name="recipients", on_delete=models.SET_NULL, null=True
    )
    transaction_sender = models.ForeignKey(SimpleUser, related_name="senders", on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20, null=False)
    transaction_date = models.DateField(null=True)
