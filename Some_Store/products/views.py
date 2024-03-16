from django.shortcuts import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .custom_permissions import IsSuperUserOrStaffOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

DEFAULT_PAGE_SIZE = 10


def index(request):
    return HttpResponse('Welcome to Some Store!')


class Paginator(PageNumberPagination):
    page_size = DEFAULT_PAGE_SIZE
    page_query_param = 'page'
    display_page_controls = True


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().select_related('category_id', 'author_id')
    serializer_class = ProductSerializer
    permission_classes = [IsSuperUserOrStaffOrReadOnly]
    pagination_class = Paginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category_id', 'author_id']
    ordering_fields = ['title', 'price']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUserOrStaffOrReadOnly]
    pagination_class = Paginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['name', 'id']
