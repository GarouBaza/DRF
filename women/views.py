
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer  # или from women.serializers


class WomenApiView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer