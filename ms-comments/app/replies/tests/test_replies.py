from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core.comments import Reply, Comment


CREATE_REPLY_URL = reverse("replies:create")
UPDATE_REPLY_URL = reverse("replies:retrieve", args=[1])
LIST_REPLIES_BY_COMMENT_URL = reverse("replies:comment", args=[1])
LIST_REPLIES_BY_USER_URL = reverse("replies:user", args=[1])


class ReplyTest(TestCase):
    def setUp(self):
        self.comment = Comment.objects.create(
            article=1,
            user=1,
            body="This is my first comment",
            status=True,
        )
        self.reply = Reply.objects.create(
            comment=self.comment,
            user=1,
            body="This is my first reply",
            status=True,
        )
        assert (
            self.comment.id is not None
        ), "Comment object was not created successfully"
        assert self.reply.id is not None, "Reply object was not created successfully"
        self.update_reply_url = reverse("replies:retrieve", args=[self.reply.id])
        self.client = APIClient()

    def test_create_reply_success(self):
        payload = {
            "body": "This is my first reply",
            "user": 1,
            "comment_id": self.comment.id,
        }
        res = self.client.post(CREATE_REPLY_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        reply = Reply.objects.get(id=res.data["data"]["id"])
        self.assertEqual(reply.body, payload["body"])

    def test_list_replies_by_comment_success(self):
        res = self.client.get(LIST_REPLIES_BY_COMMENT_URL, {"comment": 1})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_replies_by_user_success(self):
        res = self.client.get(LIST_REPLIES_BY_USER_URL, {"user": 1})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_replies_update_status_code(self):

        res = self.client.put(
            self.update_reply_url,
            {
                "id": self.reply.id,
                "user": 1,
                "comment_id": self.comment.id,
                "comment": self.comment,
                "body": "This is my first reply",
                "status": True,
            },
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
