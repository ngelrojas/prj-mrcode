from django.urls import path
from .custom_login import CustomTokenObtainPairView
from .views import CreateUserView, UserViewSet, UsersPublic, UserPublic

app_name = "user"

urlpatterns = [
    path("login", CustomTokenObtainPairView.as_view(), name="login"),
    path("user", CreateUserView.as_view(), name="create"),
    path(
        "user/<int:pk>",
        UserViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
            }
        ),
        name="update",
    ),
    path(
        "user/public",
        UsersPublic.as_view(
            {
                "get": "list",
            }
        ),
        name="list",
    ),
    path(
        "user/public/<int:pk>",
        UserPublic.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="retrieve",
    ),
]
