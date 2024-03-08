from rest_framework import serializers
from core.post import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("id",)

    def create(self, validated_data):
        user_id = self.context["request"].user
        post = Post.objects.create(author=user_id, **validated_data)
        return post
