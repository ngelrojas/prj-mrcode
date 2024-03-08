from django.urls import path
from .views import CreatePostView

app_name = "articles"

urlpatterns = [
    path("article", CreatePostView.as_view({"post": "create"}), name="create"),
]