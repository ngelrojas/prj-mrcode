from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core.post import Post

CREATE_POST_URL = reverse("articles:create")
RETRIEVE_POST_URL = reverse("articles:retrieve", args=[1])


class PostTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_post_success(self):
        payload = {
            "title": "My first post",
            "content": "This is my first post",
            "summary": "this is a summary",
            "author": 1,
        }
        res = self.client.post(CREATE_POST_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        post = Post.objects.get(id=res.data["data"]["id"])
        self.assertEqual(post.title, payload["title"])
        self.assertEqual(post.content, payload["content"])

    def test_create_post_failure(self):
        payload = {
            "title": "My first post",
        }
        res = self.client.post(CREATE_POST_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data["content"][0], "This field is required.")

    def test_list_articles_success(self):
        res = self.client.get(CREATE_POST_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_articles_by_author_success(self):
        res = self.client.get(RETRIEVE_POST_URL, {"author": 1})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
