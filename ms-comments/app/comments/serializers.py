from rest_framework import serializers
from core.comments import Comment, Reply


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
