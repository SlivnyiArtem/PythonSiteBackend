from django.db import models


class Card(models.Model):
    card_number = models.IntegerField(primary_key=True)
    MM = models.IntegerField(max_length=255)
    YY = models.IntegerField(max_length=255)
    bank = models.CharField(null=False)
    system = models.CharField(null=False)

    def __str__(self):
        return str(self.card_number)

    def get_dictionary_deserialize(self):
        serialize_dict = {"card_number": self.card_number}
        return serialize_dict
