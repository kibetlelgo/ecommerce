from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

ORDER_STATUSES =(
    ("Pending", "Pending"),
    ("Completed", "Completed"),
    ("Delivered", "Delivered")
)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='orders')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUSES, default='Pending')

