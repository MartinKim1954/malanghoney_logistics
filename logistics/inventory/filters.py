from .models import Inventory
import django_filters


class InventoryFilter(django_filters.FilterSet):
    class Meta:
        model = Inventory
