from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import CommonUser


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        label="confirm password",
        allow_null=False,
        allow_blank=False,
        write_only=True
    )

    token = serializers.CharField(read_only=True)

    class Meta:
        model = CommonUser
        fields = ["id", "username", "password", "confirm_password", "token"]

    extra_kwargs = {
        "id": {
            "read_only": True
        },
        "username": {
            "min_length": 6,
            "max_length": 20,
            "error_message": {
                "min_length": "the length of name is too short",
                "max_length": "the length of name is too long"
            },
            "required": True
        },
        "password": {
            "write_only": True,
            "min_length": 8,
            "max_length": 20,
            "error_message": {
                "min_length": "the length of password is too short",
                "max_length": "the length of password is too long"
            },
            "required": True
        },
        "confirm_password": {
            "read_only": True,
            "required": True
            }
    }

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError("password mismatch")
        return attrs

    def create(self, validated_data):
        del validated_data["confirm_password"]

        user = super().create(validated_data)
        user.set_password(validated_data.get("password"))
        user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token

        return user