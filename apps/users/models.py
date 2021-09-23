from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from rest_framework.exceptions import AuthenticationFailed, ValidationError


class UserManager(BaseUserManager):
    def _create_user(
        self, email, password, is_staff, is_superuser, **extra_fields
    ):
        """
        Creates and saves a User with the given username, email and password.
        """
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        is_staff = extra_fields.pop("is_staff", False)
        is_superuser = extra_fields.pop("is_superuser", False)
        return self._create_user(
            email, password, is_staff, is_superuser, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid4(), editable=False, unique=True)
    username = models.CharField(
        verbose_name="Username",
        max_length=150,
        unique=True,
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField(
        verbose_name="Email", unique=True, max_length=255, blank=True
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    # Fields settings
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        db_table = "user"

    def __str__(self):
        return self.username

    @classmethod
    def is_username_taken(cls, username):
        user = cls.objects.filter(username=username)
        if not user.exists():
            return False
        return True

    @classmethod
    def is_email_taken(cls, email):
        user = cls.objects.filter(email=email)
        if not user.exists():
            return False
        return True

    def update_username(self, username):
        if self.is_username_taken(username) and self.username != username:
            raise ValidationError("The username is already taken.")

        self.username = username
        self.save()

    def update_email(self, email):
        if self.is_email_taken(email) and self.email != email:
            raise ValidationError("The email is already taken.")

        self.email = email
        self.save()

    def update_password(self, password):
        self.set_password(password)
        self.save()

    def update(self, username=None, password=None, email=None, save=True):
        if username:
            self.update_username(username=username)

        if email:
            self.update_email(email=email)

        if password:
            self.update_password(password=password)

        if save:
            self.save()

    def delete_with_password(self, password):
        if not self.check_password(password):
            raise AuthenticationFailed("Wrong password.")
        self.delete()
