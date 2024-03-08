from rest_framework import serializers
from core.category import Category
from core.post import Post
from categories.serializers import CategorySerializerPublic


class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        categories = validated_data.pop('category')
        post = Post.objects.create(**validated_data)
        post.category.set(categories)
        return post


class PostSerializerPublic(serializers.ModelSerializer):
    category = CategorySerializerPublic(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
