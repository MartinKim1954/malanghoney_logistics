from django.urls import path
from . import views

urlpatterns = [
    path('/register', views.inventory_list),
    # path('/summary', views.summary),
]
