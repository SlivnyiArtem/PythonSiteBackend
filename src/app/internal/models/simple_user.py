from django.db import models
from rest_framework import status

from app.internal.models.auth_user import AuthUser
from app.internal.transport.messages import common_messages


class SimpleUser(models.Model):
    # user_auth = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    simple_user_id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    full_username = models.CharField(max_length=255, null=True)
    user_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.BigIntegerField(null=True, blank=True)
    friends = models.ManyToManyField(to="self", related_name="f", symmetrical=False, blank=True)
    hash_of_password = models.CharField(max_length=255, null=True, default=None, editable=True, blank=True)
    login_access = models.BooleanField(default=True)

    def __str__(self):
        return str(self.simple_user_id)

    @staticmethod
    def get_dictionary_deserialize(user, code: str) -> dict:
        serialize_dict = (
            vars(user)
            if (user is not None and code == status.HTTP_200_OK)
            else {"error_message": common_messages.MESSAGE_DICT.get(code)}
        )
        serialize_dict["friends"] = list(map(lambda f: f.full_username, user.friends.all()))
        serialize_dict.update(error_code=code)
        if code == status.HTTP_200_OK:
            serialize_dict.pop("_state")
        return serialize_dict
