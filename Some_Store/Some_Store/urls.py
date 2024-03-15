from django.contrib import admin
from django.urls import path
from rest_framework import routers

from products.views import index, ProductViewSet, CategoryViewSet
from .swagger import urlpatterns as doc_urls

router = routers.SimpleRouter()

router.register(r'api/v1/products', ProductViewSet, basename='Products')
router.register(r'api/v1/category', CategoryViewSet, basename='Category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]

urlpatterns += router.urls
urlpatterns += doc_urls

