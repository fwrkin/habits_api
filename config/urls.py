from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("habits.urls", namespace="habits")),
    path("api/", include("users.urls", namespace="users")),
    path("api/auth/", include("rest_framework.urls")),
]
