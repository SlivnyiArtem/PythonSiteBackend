from django.contrib.auth import get_user_model
from rest_framework import serializers

from app.internal.models.simple_user import SimpleUser


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["user_id", "password"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUser
        fields = ["simple_user_id", "full_username", "user_name", "surname"]
