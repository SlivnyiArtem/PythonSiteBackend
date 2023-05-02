from django.db import models


class TransactionLog(models.Model):
    transaction_recipient_id = models.IntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=20, null=False)
    transaction_date = models.DateField(null=True)
    is_outgoing_transaction = models.BooleanField(null=False)
