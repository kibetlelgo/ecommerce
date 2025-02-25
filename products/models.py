from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)


    def __str__(self):
        return self.name 


class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') #category.products
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', default=None, null=True) #user.products
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
