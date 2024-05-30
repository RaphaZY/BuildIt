from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=240)
    descript = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    path = models.ImageField(upload_to="imagens/")
    stored = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=datetime.now, blank =True)
    items = models.ManyToManyField(
        Product,
        through="ItemOrder",
        through_fields=("order", "product"),
    )


class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
   