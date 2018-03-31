from django.shortcuts import render

# Create your views here.
import django_filters
from  rest_framework import viewsets,filters

from .models import Book,BookType
from .serialzier import BookSerializer,BookTypeSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookTypeViewSet(viewsets.ModelViewSet):
    queryset = BookType.objects.all()
    serializer_class = BookTypeSerializer