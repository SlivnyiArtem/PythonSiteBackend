from django.contrib.auth import authenticate, get_user_model
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


class LoginSerializer(serializers.Serializer):
    # email = serializers.CharField(max_length=255)
    # username = serializers.CharField(max_length=255, read_only=True)
    # password = serializers.CharField(max_length=128, write_only=True)
    # token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        return {data}
        email = data.get("user_id")
        password = data.get("password")
        if password is None:
            raise serializers.ValidationError("A password is required to log in.")
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError("A user with this email and password was not found.")
        if not user.is_active:
            raise serializers.ValidationError("This user has been deactivated.")
        return {"username": user.username, "token": user.password}
