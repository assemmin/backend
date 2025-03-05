from django.urls import path
from .views import (
    create_table,
    table_list,
    available_tables,
)

urlpatterns = [
    path('create/', create_table, name='table_create'),          # Создание столика
    path('list/', table_list, name='table_list'),                # Список всех столов
    path('available/', available_tables, name='available_tables'), # Доступные столики по дате
]
