from django.urls import path
from .custom_login import CustomTokenObtainPairView

app_name = "user"

urlpatterns = [
    path("login", CustomTokenObtainPairView.as_view(), name="login"),
]