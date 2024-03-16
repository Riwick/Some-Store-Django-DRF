from django.shortcuts import HttpResponse
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .custom_permissions import IsSuperUserOrStaffOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


def index(request):
    return HttpResponse('Welcome to Some Store!')


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().select_related('category_id', 'author_id')
    serializer_class = ProductSerializer
    permission_classes = [IsSuperUserOrStaffOrReadOnly]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUserOrStaffOrReadOnly]
