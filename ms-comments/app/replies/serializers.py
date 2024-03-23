from rest_framework import serializers
from core.comments import Reply
from comments.serializers import CommentSerializer


class ReplySerializer(serializers.ModelSerializer):
    comment_id = serializers.IntegerField(write_only=True)
    comment = CommentSerializer(read_only=True)

    class Meta:
        model = Reply
        fields = [
            "id",
            "user",
            "body",
            "comment_id",
            "comment",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("id",)

    def create(self, validated_data):
        comment_id = validated_data.pop("comment_id")
        reply = Reply.objects.create(comment_id=comment_id, **validated_data)
        return reply
