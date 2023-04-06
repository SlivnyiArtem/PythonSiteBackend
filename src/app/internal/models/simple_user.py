import json

from django.contrib.postgres.fields import ArrayField
from django.db import models
from rest_framework import status

from app.internal.transport.messages import common_messages


class SimpleUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.BigIntegerField(null=True)
    money_users = ArrayField(models.CharField(max_length=50, blank=True), size=10, default=list, blank=True)

    # relationships = models.JSONField(default=json.dumps({"money_friends": []}))

    def __str__(self):
        return str(self.user_id)

    @staticmethod
    def get_dictionary_deserialize(user, code: str) -> dict:
        serialize_dict = (
            vars(user)
            if (user is not None and code == status.HTTP_200_OK)
            else {"error_message": common_messages.MESSAGE_DICT.get(code)}
        )
        serialize_dict.update(error_code=code)
        if code == status.HTTP_200_OK:
            serialize_dict.pop("_state")
        return serialize_dict
