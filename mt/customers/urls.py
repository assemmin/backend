from django.urls import path
from .views import get_customers, get_customer, create_customer
from tables.views import table_list_view

urlpatterns = [
    path("", get_customers, name="customers_list"),
    path("<int:id>/", get_customer, name="customer_detail"),
    path("create/", create_customer, name="customer_create"),
    path("list/", table_list_view, name="table_list"),
]
