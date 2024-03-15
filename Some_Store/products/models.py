from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, null=False, max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(null=False, max_length=127)
    description = models.TextField(max_length=2000, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    quantity = models.PositiveIntegerField(null=False, default=1)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
