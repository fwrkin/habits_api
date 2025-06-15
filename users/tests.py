from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from users.models import User


class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "email": "testuser@example.com",
            "password": "testpassword",
            "username": "testuser",
            "telegram_id": "5106855055",
        }

    def test_register_user(self):
        data = {"username": "testuser", "email": "testuser@example.com", "password": "testpass123"}
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)  # Проверяем наличие id вместо "user"
        self.assertEqual(response.data["username"], "testuser")

    def test_login_user(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(reverse("login"), {"username": "testuser", "password": "testpass123"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("refresh", response.data)  # Проверяем токены
        self.assertIn("access", response.data)

    def test_login_invalid_credentials(self):
        """Тест авторизации с неверными данными"""
        url = reverse("users:token_obtain_pair")
        data = {"email": "wronguser@example.com", "password": "wrongpassword"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_refresh_token(self):
        """Тест обновления токена"""
        # Регистрируем пользователя и получаем токены
        User.objects.create_user(email="testuser@example.com", password="testpassword", username="testuser")
        login_url = reverse("users:token_obtain_pair")
        login_data = {"email": "testuser@example.com", "password": "testpassword"}
        login_response = self.client.post(login_url, login_data, format="json")
        refresh_token = login_response.data["refresh"]

        # Обновляем токен
        url = reverse("users:token_refresh")
        data = {"refresh": refresh_token}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
