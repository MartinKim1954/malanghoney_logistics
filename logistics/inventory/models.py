from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=20)
    inbound = models.IntegerField()
    outbound = models.IntegerField(default=0)
    registered = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inventory'
    
    def __str__(self):
        return self.name