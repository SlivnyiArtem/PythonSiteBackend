from django.db import models
from app.internal.models.simple_user import SimpleUser
from app.internal.models.banking_account import BankingAccount
from django.core.validators import MaxValueValidator, MinValueValidator


class Card(models.Model):
    card_number = models.IntegerField(primary_key=True)
    MM = models.IntegerField(max_length=255, validators=[MaxValueValidator(24), MinValueValidator(1)])
    YY = models.IntegerField(max_length=255)
    system = models.CharField(null=False, max_length=20)
    banking_account = models.OneToOneField(BankingAccount, on_delete=models.CASCADE)
    currency_amount = models.DecimalField(decimal_places=2, max_digits=20)
    card_owner = models.OneToOneField(SimpleUser, on_delete=models.CASCADE)
    # card_owner = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)

    def get_user(self):
        return self.banking_account

    def __str__(self):
        return str(self.card_number)

    def get_dictionary_deserialize(self):
        serialize_dict = {"card_number": self.card_number}
        return serialize_dict
