from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import PostSerializer, PostSerializerPublic
from core.post import Post


class CreatePostView(viewsets.ViewSet):
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()

    def list(self, request):
        try:
            queryset = Post.objects.all()
            serializer = PostSerializerPublic(queryset, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"data": serializer.data}, status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ViewSet):
    serializer_class = PostSerializerPublic
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()

    def retrieve(self, request, pk=None):
        try:
            queryset = Post.objects.filter(author=pk)
            serializer = self.serializer_class(queryset, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
