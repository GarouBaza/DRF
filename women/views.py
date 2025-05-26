from django.forms import model_to_dict
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer  # или from women.serializers

class WomenApiView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({'post': model_to_dict(post_new)})

    def delete(self,request ,id):
        delete_object = Women.objects.filter(id=id).delete()
        if delete_object == 0:
            return Response({'error': 'Women does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'delete': delete_object})


# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


