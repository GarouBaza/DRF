from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer  # или from women.serializers

class WomenApiView(APIView):
    def get(self, request):
        return Response({'title': 'Angelina Jolie'})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


