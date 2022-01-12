from django.db import models
from django.contrib import admin


class SimpleUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.name}'
