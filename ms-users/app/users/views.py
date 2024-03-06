from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, UserSerializerPublic
from core.user import User


class CreateUserView(generics.CreateAPIView):
    """Create new user"""
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserViewSet(viewsets.ViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def retrieve(self, request, pk=None):
        try:
            current_user = User.objects.get(id=request.user.id, deleted=False, is_superuser=False)
            serializer = self.serializer_class(current_user)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            current_user = User.objects.get(id=request.user.id, deleted=False, is_superuser=False)
            serializer = self.serializer_class(current_user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            current_user = User.objects.get(id=request.user.id, deleted=False, is_superuser=False)
            current_user.deleted = True
            current_user.is_active = False
            current_user.save()
            return Response({"data": "user deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UsersPublic(viewsets.ViewSet):
    serializer_class = UserSerializerPublic
    permission_classes = (AllowAny,)

    def list(self, request):
        try:
            queryset = User.objects.filter(deleted=False).exclude(is_superuser=True)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserPublic(viewsets.ViewSet):
    serializer_class = UserSerializerPublic
    permission_classes = (AllowAny,)

    def retrieve(self, request, pk=None):
        try:
            current_user = User.objects.get(id=pk, deleted=False, is_superuser=False)
            serializer = self.serializer_class(current_user)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
