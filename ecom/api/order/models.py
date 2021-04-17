from django.db import models
from api.user.models import CustomUser
from api.product.models import Product

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    product_names = models.CharField(max_length=500)
    total_products = models.CharField(default=0, max_length=500)
    transaction_id = models.CharField(default=0, max_length=150)
    total_amount = models.CharField(default=0, max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
