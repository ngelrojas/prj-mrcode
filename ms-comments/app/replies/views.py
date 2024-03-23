from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.comments import Reply
from .serializers import ReplySerializer


class ReplyBaseView(viewsets.ViewSet):
    serializer_class = ReplySerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, pk=None, filter_field=None):
        try:
            filter_kwargs = {filter_field: pk} if filter_field else {}
            queryset = Reply.objects.filter(**filter_kwargs)
            serializer = self.serializer_class(queryset, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ReplyView(ReplyBaseView):

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            instance = Reply.objects.get(id=pk)
            serializer = self.serializer_class(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = Reply.objects.get(id=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ReplyListUser(ReplyBaseView):

    def retrieve(self, request, pk=None, **kwargs):
        return super().retrieve(request, pk, filter_field="user")


class ReplyListComments(ReplyBaseView):

    def retrieve(self, request, pk=None, **kwargs):
        return super().retrieve(request, pk, filter_field="comment")
