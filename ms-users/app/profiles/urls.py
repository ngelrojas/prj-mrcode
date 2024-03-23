from django.urls import path
from .views import CreateProfileView, ProfileViewSet, ProfilesPublic, ProfilePublic

app_name = "profile"

urlpatterns = [
    path("profile", CreateProfileView.as_view({"post": "create"}), name="create"),
    path("profile/<int:pk>", ProfileViewSet.as_view({
        "get": "retrieve",
        "put": "update",
    }), name="update"),
    path("profile/public", ProfilesPublic.as_view({
        "get": "list",
    }), name="list"),
    path("profile/public/<int:pk>", ProfilePublic.as_view({
        "get": "retrieve",
    }), name="retrieve"),
]
