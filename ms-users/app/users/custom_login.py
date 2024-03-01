from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            token = response.data
            return Response({'token': token['access']})
        except Exception as ex:
            return Response({
                'data': 'error',
                'detail': format(ex),
            })
