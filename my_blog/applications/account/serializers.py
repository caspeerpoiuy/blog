from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from my_blog import settings
from utils.function import generate_verify_email_url
from .models import CommonUser, UserCode


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        label="confirm password",
        allow_null=False,
        allow_blank=False,
        write_only=True
    )
    code = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        write_only=True
    )

    token = serializers.CharField(read_only=True)

    class Meta:
        model = CommonUser
        fields = ["id", "username", "password", "confirm_password", "token", "code"]

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

    def validate_code(self, value):
        # try:
        sql_code = UserCode.objects.get(code=value)
        if sql_code is None:
            raise serializers.ValidationError("this code not exists")
        if sql_code.active is False:
            raise serializers.ValidationError("the code status error")
        return value
        # except Exception as e:
        #     print(e)

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError("password mismatch")
        return attrs

    def create(self, validated_data):
        del validated_data["confirm_password"]

        code = UserCode.objects.get(code=validated_data.get("code"))
        code.active = False
        code.save()

        del validated_data["code"]

        user = super().create(validated_data)
        user.set_password(validated_data.get("password"))
        user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token

        return user


class UserBaseInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommonUser
        fields = ["id", "username", "avatar_uri"]


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommonUser
        fields = ["id", "email"]
        extra_kwargs = {
            "email": {
                "required": True
            }
        }

    def update(self, instance, validated_data):
        print(instance.id)
        email = validated_data.get("email")
        instance.email = email
        instance.save()
        subject = "casperblog激活邮件"
        message = ""
        from_email = settings.EMAIL_FROM
        recipient_list = [email, "casperblog@163.com"]
        verify_url = generate_verify_email_url(instance.id, email)
        html_message = "<p>casperblog激活邮件</p> "\
                       "<p><a href='%s'>%s</a></p>" %(email, verify_url)
        from celery_tasks.email.tasks import send_verify_mail
        send_verify_mail.delay(subject, message, from_email, recipient_list, html_message)
        return instance