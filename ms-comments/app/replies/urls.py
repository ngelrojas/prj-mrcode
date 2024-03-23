from django.urls import path
from .views import ReplyView, ReplyListUser, ReplyListComments

app_name = "replies"

urlpatterns = [
    path("", ReplyView.as_view({"post": "create"}), name="create"),
    path(
        "<int:pk>",
        ReplyView.as_view({"put": "update", "delete": "destroy"}),
        name="retrieve",
    ),
    path("user/<int:pk>", ReplyListUser.as_view({"get": "retrieve"}), name="user"),
    path(
        "comment/<int:pk>",
        ReplyListComments.as_view({"get": "retrieve"}),
        name="comment",
    ),
]
