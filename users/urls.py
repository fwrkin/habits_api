from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from .views import RegisterView, LoginView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(permission_classes=(AllowAny,)), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
]
