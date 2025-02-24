from rest_framework import serializers
from .models import BookModel, AuthorModel

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ("first_name", "last_name")

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookModel
        fields = ("title", "price", "publish_date", "author")