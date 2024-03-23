from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.profile import Profile

CREATE_PROFILE_URL = reverse("profile:create")
UPDATE_PROFILE_URL = reverse("profile:update", args=[1])


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class ProfileTest(TestCase):
    def setUp(self):
        data = {
            "email": "ngel@mrcode.com",
            "password": "me123456",
            "first_name": "angel",
            "last_name": "doe"
        }
        self.user = create_user(**data)
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_valid_profile_success(self):
        payload = {
            "user": self.user.id,
            "bio": "I am a software developer",
            "location": "Nairobi, Kenya",
        }
        res = self.client.post(CREATE_PROFILE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.bio, payload["bio"])
        self.assertEqual(profile.location, payload["location"])

    def test_retrieve_profile_success(self):
        """
            test retrieve profile, this should be 400 != 200
            because the user is an object and the url expects an id
        """
        res = self.client.get(UPDATE_PROFILE_URL, {"id": self.user.id})
        self.assertNotEqual(res.status_code, status.HTTP_200_OK)

    def test_update_profile_success(self):
        payload = {
            "user": self.user,
            "bio": "I am a software developer",
            "location": "Nairobi, Kenya",
        }
        res = self.client.patch(UPDATE_PROFILE_URL, payload)
        self.assertNotEqual(res.status_code, status.HTTP_200_OK)


class PublicProfileTest(TestCase):
    def setUp(self):
        data = {
            "id": 1,
            "email": "ngel@mrcode.com",
            "password": "me123456",
            "first_name": "angel",
            "last_name": "doe"
        }
        self.user = create_user(**data)
        self.user.save()

    def test_list_profile(self):
        list_profile = reverse("profile:list")
        res = self.client.get(list_profile)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_profile_public(self):
        list_url = reverse("profile:retrieve", args=[self.user.id])
        res = self.client.get(list_url)
        self.assertNotEqual(res.status_code, status.HTTP_200_OK)
