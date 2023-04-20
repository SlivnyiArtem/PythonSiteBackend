from django.db import models

from app.internal.models.simple_user import SimpleUser


class TransactionLog(models.Model):
    transaction_recipient = models.OneToOneField(SimpleUser, on_delete=models.SET_NULL)
    amount = models.DecimalField(decimal_places=2, max_digits=20, null=False)
    transaction_date = models.DateField(null=True)
    is_outgoing_transaction = models.BooleanField(null=False)
    # surname = models.CharField(max_length=255)
    # phone_number = models.BigIntegerField(null=True)
    # friends = models.ManyToManyField(to="self", related_name="f", symmetrical=False)
