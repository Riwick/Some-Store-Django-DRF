from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers

from products.views import index, ProductViewSet, CategoryViewSet
from .swagger import urlpatterns as doc_urls

router = routers.SimpleRouter()

router.register(r'products', ProductViewSet, basename='Products')
router.register(r'category', CategoryViewSet, basename='Category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
]

urlpatterns += router.urls
urlpatterns += doc_urls

