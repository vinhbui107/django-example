from django.apps import apps


def get_user_model():
    return apps.get_model("users", "User")
