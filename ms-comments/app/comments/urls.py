from django.urls import path
from .views import CommentViewSet, CommentListUser, CommentListArticles

app_name = "comments"

urlpatterns = [
    path(
        "",
        CommentViewSet.as_view({"post": "create"}),
        name="create",
    ),
    path(
        "<int:pk>",
        CommentViewSet.as_view(
            {
                "put": "update",
                "delete": "destroy",
            }
        ),
        name="retrieve",
    ),
    path("user/<int:pk>", CommentListUser.as_view({"get": "retrieve"}), name="user"),
    path(
        "article/<int:pk>",
        CommentListArticles.as_view({"get": "retrieve"}),
        name="article",
    ),
]
