from django.db import models

from app.internal.models.simple_user import SimpleUser


class RefreshToken(models.Model):
    Jti = models.CharField(null=False, max_length=10000, primary_key=True)
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
