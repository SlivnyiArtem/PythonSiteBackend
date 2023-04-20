from django.db import models
from rest_framework import status

from app.internal.models.transaction_log import TransactionLog
from app.internal.transport.messages import common_messages

#
# class CustomUser(models.Model):
#     user_id = models.IntegerField(primary_key=True)
#     followers = models.ManyToManyField(to="self", related_name="followees", symmetrical=False)


class SimpleUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    full_username = models.CharField(max_length=255, null=True)
    user_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.BigIntegerField(null=True)
    friends = models.ManyToManyField(to="self", related_name="f", symmetrical=False, blank=True)
    transactions_history = models.ManyToManyField(TransactionLog, blank=True)

    # friends = models.ManyToManyField("SimpleUser", symmetrical=False, blank=True)
    # friends = models.ManyToManyField('self', through='FriendBackLoop',
    #                                  symmetrical=False)
    # friends = models.ManyToManyField(
    #     'self',
    #
    #     # recursive relationships to self with intermediary
    #     # through model are always defined as non-symmetrical
    #     symmetrical=False,
    #
    #     # through='SimpleUserFriend',
    #
    #     # this argument is required to define a custom
    #     # through model for many to many relationship to self
    #     # position matters: 1 - source (from), 2 - target (to)
    #     # through_fields=('person', 'friend'),
    # )

    # friends = ArrayField(models.ForeignKey(SimpleUser, on_delete=), default=list, blank=True)
    # friends = ArrayField(models.CharField(max_length=50, blank=True), size=10, default=list, blank=True)

    def __str__(self):
        return str(self.user_id)

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


# class SimpleUserFriend(models.Model):
#     # required relationship-defining foreign keys
#     # (note that the order does not matter, it matters
#     # in 'through_fields' argument in 'friends' field of the 'Person' model)
#     person = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
#     friend = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)


# class Person(models.Model):
#     name = models.CharField(max_length = 255)
#     occupation = models.CharField(max_length = 255)
#     friends = models.ManyToManyField('self', through = 'PersonFriends',
#           symmetrical = False)
#     #     ^^^^^^^^^^^
#     # This has to be false when using `through` models. Or else your
#     # model will not validate.


# class FriendBackLoop(models.Model):
#     person = models.ForeignKey(SimpleUser, related_name="a", on_delete=models.CASCADE)
#     friend = models.ForeignKey(SimpleUser, related_name="b", on_delete=models.CASCADE)
#     # source = models.ForeignKey(SimpleUser, related_name = 's', on_delete=models.CASCADE)
#     # #                                  ^^^^^^^^^^^^
#     # # You need different `related_name` for each when you have
#     # # multiple foreign keys to the same table.
#     #
#     # target = models.ForeignKey(SimpleUser, related_name = 't', on_delete=models.CASCADE)
#     # comment = models.CharField(max_length = 255)
