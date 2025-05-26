from django.forms import model_to_dict
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer  # или from women.serializers

class WomenApiView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if Women.objects.filter(
                title=request.data['title'],
                content=request.data['content'],
                cat_id=request.data['cat_id']
        ).exists():
            return Response(
                {"error": "Такой пост уже существует."},
                status=status.HTTP_400_BAD_REQUEST
            )

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({'post': WomenSerializer(post_new).data})

    def delete(self,request ,id):
        delete_object = Women.objects.filter(id=id).delete()
        if delete_object == 0:
            return Response({'error': 'Women does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'delete': delete_object})


# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


