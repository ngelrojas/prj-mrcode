from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create new user"""
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
