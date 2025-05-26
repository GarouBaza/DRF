import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Women



class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=False)
    cat_id = serializers.IntegerField()




# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# def encode():
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     models_sr = WomenSerializer(model)
#     print(models_sr.data, type(models_sr.data), sep='\n')
#     json = JSONRenderer().render(models_sr.data)
#     print(json)
#
#
# def decode():
#     json_bytes = b'{"title": "Angelina Jolie", "content": "Content: Angelina Jolie"}'
#     stream = io.BytesIO(json_bytes)
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     if serializer.is_valid():
#         print(serializer.validated_data)