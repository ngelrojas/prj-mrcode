from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import PostSerializer
from core.post import Post


class CreatePostView(viewsets.ViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
