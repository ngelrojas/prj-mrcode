from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse("user:create")
UPDATE_USER_URL = reverse("user:update", args=[1])


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class UserManagerTests(TestCase):
    def test_create_user(self):
        current_user = get_user_model()
        user = current_user.objects.create_user(
            email="ngel@mrcode.com",
            password="me123456"
        )
        self.assertEqual(user.email, "ngel@mrcode.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        current_user = get_user_model()
        user = current_user.objects.create_superuser(
            "admin@mrcode.com",
            "admin2024"
        )
        self.assertEqual(user.email, "admin@mrcode.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class UserTest(TestCase):
    def setUp(self):
        data = {
            "id": 1,
            "email": "ngel@mrcode.com",
            "password": "me123456",
            "first_name": "angel",
            "last_name": "doe"
        }
        self.user = create_user(**data)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_valid_user_success(self):
        payload = {
            "email": "angel@mrcode.com",
            "password": "me123456",
            "first_name": "angel",
            "last_name": "doe"
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_user_exists(self):
        payload = {
            "email": "angel@mrcode.com",
            "password": "me123456",
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        payload = {
            "email": "nagel@mrcode.com",
            "password": "me",
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload["email"]
        ).exists()
        self.assertFalse(user_exists)

    def test_update_data_user(self):
        payload = {
            "email": "angel@mrcode.com",
            "password": "me123456",
            "first_name": "angel",
            "last_name": "doe"
        }
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, payload["first_name"])
        self.assertTrue(self.user.check_password(payload["password"]))

    def test_retrieve_user(self):

        res = self.client.get(UPDATE_USER_URL, {"id": 1})
        self.user.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        payload = {
            "first_name": "angel",
            "last_name": "doe",
        }
        update_url = reverse("user:update", args=[self.user.id])
        res = self.client.put(update_url, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        delete_url = reverse("user:update", args=[self.user.id])
        res = self.client.delete(delete_url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


class UserTestPublic(TestCase):
    def setUp(self):
        data = {
            "id": 1,
            "email": "ngel@mrcode.com",
            "password": "me123456",
            "first_name": "angel",
            "last_name": "doe"
        }
        self.user = create_user(**data)

    def test_list_user_public(self):
        list_url = reverse("user:list")
        res = self.client.get(list_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_user_public(self):
        list_url = reverse("user:retrieve", args=[self.user.id])
        res = self.client.get(list_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
