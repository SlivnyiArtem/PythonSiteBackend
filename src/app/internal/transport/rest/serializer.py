# from django.contrib.auth import authenticate, get_user_model
# from django.core.exceptions import ValidationError
# from rest_framework import serializers
#
# from app.internal.models.auth_user import AuthUser
# from app.internal.models.simple_user import SimpleUser
#
#
# class UserAuthSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ["user_id", "password"]
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SimpleUser
#         fields = ["simple_user_id", "full_username", "user_name", "surname"]
#
#
# class LoginSerializer(serializers.Serializer):
#     user_id = serializers.IntegerField()
#     password = serializers.CharField(max_length=255)
#
#     def to_internal_value(self, data):
#         user_id = data.get("user_id")
#         password = data.get("password")
#
#         return {"user_id": user_id, "password": password}
#
#     def to_representation(self, instance):
#         return {"user_id": instance.user_id, "password": instance.password}
#
#     def create(self, validated_data):
#         return AuthUser.objects.create(**validated_data)
#
#     # token = serializers.CharField(max_length=255, read_only=True)
#
#     # def is_valid(self, *, raise_exception=False):
#     #     assert hasattr(self, "initial_data"), (
#     #         "Cannot call `.is_valid()` as no `data=` keyword argument was "
#     #         "passed when instantiating the serializer instance."
#     #     )
#     #
#     #     if not hasattr(self, "_validated_data"):
#     #         try:
#     #             self._validated_data = self.run_validation(self.initial_data)
#     #         except ValidationError as exc:
#     #             self._validated_data = {}
#     #             self._errors = exc.detail
#     #         else:
#     #             self._errors = {}
#     #
#     #     if self._errors and raise_exception:
#     #         raise ValidationError(self.errors)
#     #
#     #     raise Exception(str(hasattr(self, "_validated_data")) + "@")
#     #
#     #     return not bool(self._errors)
#
#     def validate(self, data):
#         # return data
#         user_id = data.get("user_id")
#         password = data.get("password")
#         if password is None:
#             raise serializers.ValidationError("A password is required to log in.")
#
#         user = authenticate(username=user_id, password=password)
#
#         if user is None:
#             raise serializers.ValidationError("A user with this email and password was not found.")
#         if not user.is_active:
#             raise serializers.ValidationError("This user has been deactivated.")
#
#         return data
