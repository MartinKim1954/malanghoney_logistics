from django.shortcuts import render

from django_tables2 import SingleTableView

from .models import Inventory
from .tables import InventoryTable

# Create your views here.
class InventoryListView(SingleTableView):
    model = Inventory
    table_class = InventoryTable
    template_name = 'register.html'