from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list_view, name='todo_lists'),  # Главная страница списка TODO
]

