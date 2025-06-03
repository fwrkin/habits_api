from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("habits.urls", namespace="habits")),
    path("users/", include("users.urls", namespace="users")),
    ]
