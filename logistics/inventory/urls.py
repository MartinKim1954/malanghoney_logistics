from django.urls import path
from . import views

urlpatterns = [
    path('/register', views.InventoryListView.as_view()),
    # path('/summary', views.summary),
]
