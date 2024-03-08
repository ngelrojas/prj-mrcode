from django.db import models
from .category import Category


class Post(models.Model):
    title = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='images/posts/%Y/%m/%d/', blank=True)
    video_link = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.IntegerField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
