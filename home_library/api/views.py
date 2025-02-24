from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.throttling import AnonRateThrottle
import json

from .serializers import AuthorSerializer, BookSerializer
from .models import AuthorModel, BookModel

# Create your views here.
class PublicLibrary(APIView):
    throttle_classes = [AnonRateThrottle]
    

    def get(self, request, format=None):
        serializer_class = BookSerializer
        content = BookModel.objects.all()
        return Response(serializer_class(content, many=True).data)
    
    def post(self, request, format=None):
        data = json.loads(request.body)
        serialized = BookSerializer(data=data)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        return Response(serialized.errors, status=400)
