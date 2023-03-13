from app.internal.models.banking_account import BankingAccount
from app.internal.models.simple_user import SimpleUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Card(models.Model):
    card_number = models.IntegerField(primary_key=True)
    MM = models.IntegerField(validators=[MaxValueValidator(12),
                                         MinValueValidator(1)])
    YY = models.IntegerField()
    system = models.CharField(null=False, max_length=20)
    banking_account = models.OneToOneField(BankingAccount,
                                           on_delete=models.CASCADE)
    # currency_amount = banking_account.related_model.currency_amount
    # card_owner = banking_account.related_model.account_owner

    #!!!
    # currency_amount = models.DecimalField(decimal_places=2, max_digits=20)
    # card_owner = models.OneToOneField(SimpleUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.card_number)

    def get_dictionary_deserialize(self):
        serialize_dict = {"card_number": self.card_number}
        return serialize_dict
