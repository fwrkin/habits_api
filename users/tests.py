from unittest import TestCase

from rest_framework import status
from django.urls import reverse


class APIClient:
    pass


class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        data = {"username": "testuser", "email": "testuser@example.com", "password": "testpass123"}
        response = self.client.post(reverse("users:register"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("user", response.data)

    def test_login_user(self):
        # Сначала зарегистрируйте пользователя
        self.client.post(
            reverse("users:register"),
            {"username": "testuser", "email": "testuser@example.com", "password": "testpass123"},
        )
        response = self.client.post(
            reverse("api-auth:token_obtain_pair"), {"username": "testuser", "password": "testpass123"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_login_invalid_credentials(self):
        url = reverse("api-auth:token_obtain_pair")
        response = self.client.post(url, {"username": "wronguser", "password": "wrongpass"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_refresh_token(self):
        login_url = reverse("api-auth:token_obtain_pair")
        login_response = self.client.post(login_url, {"username": "testuser", "password": "testpass123"})
        refresh_token = login_response.data["refresh"]
        refresh_url = reverse("api-auth:token_refresh")
        refresh_response = self.client.post(refresh_url, {"refresh": refresh_token})
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn("access", refresh_response.data)
