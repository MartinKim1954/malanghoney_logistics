from django.contrib import admin
from .models import Inventory, InAndOutBound

# Register your models here.
admin.site.register(Inventory)
admin.site.register(InAndOutBound)
