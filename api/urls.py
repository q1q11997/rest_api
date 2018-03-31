# coding: utf-8

from rest_framework import routers
from .views import BookViewSet, BookTypeViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'bookTypes', BookTypeViewSet)