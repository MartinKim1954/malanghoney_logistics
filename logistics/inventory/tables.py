import django_tables2 as tables
from .models import Inventory


class InventoryTable(tables.Table):
    class Meta:
        model = Inventory
        template_name = "django_tables2/bootstrap.html"
        sequence = ("brand", "name", "inbound")
        exclude = ("id", "outbound", "registered")
