from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from apps.users.models import User
from apps.users.forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    search_fields = ("username", "email")
    list_display = ("id", "username", "email", "is_active", "is_staff")

    fieldsets = [
        ["Auth", {"fields": ["username", "email", "password"]}],
        [
            "Settings",
            {
                "fields": [
                    # "groups",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ]
            },
        ],
        ["Important dates", {"fields": ["last_login", "date_joined"]}],
    ]

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        [
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "username",
                    "password1",
                    "password2",
                ],
            },
        ],
    ]

    ordering = ["id"]
    list_filter = ("is_staff", "is_active")
    readonly_fields = ("last_login", "date_joined")


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# Unregister the Group model from admin.
admin.site.unregister(Group)
