from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import update_last_login

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.validators import (
    user_username_exists,
    username_not_taken_validator,
    username_characters_validator,
    email_not_taken_validator,
)
from apps.common.model_loaders import get_user_model


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User

        fields = ("username", "email", "is_staff", "date_joined", "last_login")


class LoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField(
        max_length=150,
        validators=[username_characters_validator, user_username_exists],
        allow_blank=False,
    )
    password = serializers.CharField(max_length=128, allow_blank=False)

    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)
        token["user_id"] = user.id
        update_last_login(None, user)
        return token


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        validators=[
            username_characters_validator,
            username_not_taken_validator,
        ],
    )
    password = serializers.CharField(max_length=128, validators=[validate_password])
    email = serializers.EmailField(
        required=False,
        validators=[email_not_taken_validator],
    )


class UpdateUserSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        validators=[username_characters_validator],
        required=False,
        allow_blank=False,
    )
    password = serializers.CharField(
        max_length=128,
        validators=[validate_password],
        required=False,
        allow_blank=False,
    )
    email = serializers.EmailField(
        required=False,
        allow_blank=False,
    )


class DeleteUserSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, allow_blank=False)
