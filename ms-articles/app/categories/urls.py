from django.urls import path
from .views import CreateCategoryView

app_name = "categories"

urlpatterns = [
    path("category/", CreateCategoryView.as_view({"post": "create"}), name="create"),
]