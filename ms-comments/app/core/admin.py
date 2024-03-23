from django.contrib import admin
from .comments import Comment, Reply

admin.site.register(Comment)
admin.site.register(Reply)
