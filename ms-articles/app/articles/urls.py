from django.urls import path
from .views import CreatePostView, PostViewSet

app_name = "articles"

urlpatterns = [
    path("article", CreatePostView.as_view({"post": "create", "get": "list"}), name="create"),
    path("article/<int:pk>", PostViewSet.as_view({"get": "retrieve"}), name="retrieve"),
]