from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import CategorySerializer
from core.category import Category


class CreateCategoryView(viewsets.ViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

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