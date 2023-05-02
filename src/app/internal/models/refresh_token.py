# класс refresh-token
# access-token не нужно хранить в БД, он существует только во время сессии
from django.db import models

from app.internal.models.simple_user import SimpleUser


class RefreshToken(models.Model):
    Jti = models.CharField(null=False, max_length=10000)
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    token_type = models.CharField(null=False, max_length=20)
