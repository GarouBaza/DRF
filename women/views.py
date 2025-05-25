from rest_framework import generics
from django.shortcuts import render

from models import Women
from serializers import WomenSerializer
# Create your views here.


class WomenApiView(generics):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer