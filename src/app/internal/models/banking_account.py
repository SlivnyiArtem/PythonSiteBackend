from django.db import models

from app.internal.models.simple_user import SimpleUser


class BankingAccount(models.Model):
    account_number = models.IntegerField(primary_key=True)
    account_owner = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    currency_amount = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return str(self.account_number)

    def get_dictionary_deserialize(self) -> dict:
        serialize_dict = {"card_number": self.account_number}
        return serialize_dict
