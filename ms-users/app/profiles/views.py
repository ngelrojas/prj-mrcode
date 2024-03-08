from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ProfileSerializer, ProfileSerializerPublic
from core.profile import Profile


class CreateProfileView(viewsets.ViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e),}, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def retrieve(self, request, pk=None):
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializerPublic(profile)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = self.serializer_class(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProfilesPublic(viewsets.ViewSet):
    serializer_class = ProfileSerializerPublic
    permission_classes = (AllowAny,)

    def list(self, request):
        try:
            queryset = Profile.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProfilePublic(viewsets.ViewSet):
    serializer_class = ProfileSerializerPublic
    permission_classes = (AllowAny,)

    def retrieve(self, request, pk=None):
        try:
            profile = Profile.objects.get(id=pk)
            serializer = self.serializer_class(profile)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
