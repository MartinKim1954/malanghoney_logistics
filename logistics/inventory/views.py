from django.shortcuts import render
from .models import Inventory
from .tables import InventoryTable


def inventory_list(request):
    table = InventoryTable(Inventory.objects.all())
    return render(request, "register.html", {"table": table})

# from django_filters.views import FilterView
# from django_tables2.views import SingleTableMixin


# # class InventoryFilter(django_filters.FilterSet):
# #     class Meta:
# #         model = Inventory


# class FilteredInventoryListView(SingleTableMixin, FilterView):
#     table_class = InventoryTable
#     model = Inventory
#     template_name = "template.html"

#     filterset_class = InventoryFilter
