from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core.comments import Comment

CREATE_COMMENT_URL = reverse("comments:create")
UPDATE_COMMENT_URL = reverse("comments:retrieve", args=[1])
LIST_COMMENTS_BY_ARTICLE_URL = reverse("comments:article", args=[1])
LIST_COMMENTS_BY_USER_URL = reverse("comments:user", args=[1])


class CommentTest(TestCase):
    def setUp(self):
        self.comment = Comment.objects.create(
            article=1,
            user=1,
            body="This is my first comment",
            status=True,
        )
        self.client = APIClient()

    def test_create_comment_success(self):
        payload = {
            "body": "This is my first comment",
            "user": 1,
            "article": 1,
        }
        res = self.client.post(CREATE_COMMENT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        comment = Comment.objects.get(id=res.data["data"]["id"])
        self.assertEqual(comment.body, payload["body"])

    def test_list_comments_by_articles_success(self):
        res = self.client.get(LIST_COMMENTS_BY_ARTICLE_URL, {"article": 1})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_comments_by_user_success(self):
        res = self.client.get(LIST_COMMENTS_BY_USER_URL, {"user": 1})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_comments_update_status_code(self):
        res = self.client.put(UPDATE_COMMENT_URL, {"id": 1, "status": True})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
