# from django.db import models
#
# from app.internal.models.simple_user import SimpleUser
#
#
# class AccessToken(models.Model):
#     jti = models.CharField(max_length=2500, primary_key=True)
#     user = models.ForeignKey(SimpleUser, related_name="access_token", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_revoked = models.BooleanField(default=False)
#     # device_id = models.UUIDField(unique=True)
