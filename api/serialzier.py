# coding: utf-8
from rest_framework import serializers
from .models import Book,BookType

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','book_name','book_id','book_type','book_url','book_price')

class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = ('id','type_name')