from rest_framework import serializers
from core.profile import Profile
from users.serializers import UserSerializer, UserSerializerPublic


class ProfileSerializer(serializers.ModelSerializer):
    """model profile serializer"""

    class Meta:
        model = Profile
        fields = (
            "id",
            "bio",
            "photo",
            "location",
            "birth_date",
            "sn_facebook",
            "sn_twitter",
            "sn_linkedin",
            "sn_instagram",
            "sn_github",
            "sn_youtube",
            "sn_website",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        """create profile"""
        user_id = self.context["request"].user
        profile = Profile.objects.create(user=user_id, **validated_data)
        return profile


class ProfileSerializerPublic(serializers.ModelSerializer):

    user = UserSerializerPublic()

    class Meta:
        model = Profile
        fields = ("user",
                  "id",
                  "bio",
                  "photo",)
        read_only_fields = ("id",)
