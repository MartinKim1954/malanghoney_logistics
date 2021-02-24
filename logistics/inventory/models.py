from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Inventory(models.Model):
    inventory_status = models.TextField(max_length=100, default="")
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=20)
    initial_inventory = models.IntegerField()
    comment = models.TextField(max_length=200, default="")
    registered = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inventory'

    def __str__(self):
        return self.name


class InAndOutBound(models.Model):
    product_id = models.ForeignKey(
        "Inventory", on_delete=models.CASCADE, db_column="product_id")
    current_inventory = models.IntegerField()
    inbound = models.IntegerField(default=0)
    outbound = models.IntegerField(default=0)
    registered = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'in_and_out_bound'

    def __str__(self):
        return self.registered
