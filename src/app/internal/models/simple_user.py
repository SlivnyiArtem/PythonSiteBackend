from django.db import models


class SimpleUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user_id)

    def get_dictionary_deserialize(self):
        serialize_dict = vars(self)
        serialize_dict.pop("_state")
        return serialize_dict
