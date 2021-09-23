from django.contrib import admin
from django.urls import path, include

from apps.users.views import RegisterAPI, LoginAPI, UserAPI

auth_authenticated_patterns = [
    path("", UserAPI.as_view()),
    # setting api
]

auth_patterns = [
    path("login", LoginAPI.as_view()),
    path("register", RegisterAPI.as_view()),
    path("user", include(auth_authenticated_patterns)),
]

api_patterns = [
    path("auth/", include(auth_patterns)),
]

urlpatterns = [
    path("api/v1/", include(api_patterns)),
    path("admin/", admin.site.urls),
]
