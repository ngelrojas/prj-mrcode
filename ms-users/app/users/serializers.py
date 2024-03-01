from rest_framework import serializers, fields
from core.user import User


class UserSerializer(serializers.ModelSerializer):
    """model user serializer"""

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "password", "deleted")
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 5},
            "deleted": {"write_only": True},
        }
        read_only_fields = ("id",)

    def create(self, validate_data):
        """create user"""
        user_instance = User.objects.create_user(**validate_data)

        return user_instance

    def update(self, instance, validate_data):
        """update password current user"""
        password = validate_data.pop("password", None)
        user = super().update(instance, validate_data)
        if password:
            user.set_password(password)
            user.save()
        return user
