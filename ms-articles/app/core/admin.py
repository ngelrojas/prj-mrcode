from django.contrib import admin
from .post import Post
from .category import Category


admin.site.register(Post)
admin.site.register(Category)
