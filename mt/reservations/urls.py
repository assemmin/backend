from django.urls import path
from .views import (
    create_reservation,
    get_reservation,
    get_user_reservations,
    update_reservation,
    delete_reservation,
)

urlpatterns = [
    path('create/', create_reservation, name='reservation_create'),          # Создать бронь
    path('<int:id>/', get_reservation, name='reservation_detail'),           # Получить конкретную бронь
    path('user/<int:user_id>/', get_user_reservations, name='user_reservations'), # Брони пользователя
    path('<int:id>/update/', update_reservation, name='update_reservation'), # Обновить бронь
    path('<int:id>/delete/', delete_reservation, name='delete_reservation'), # Удалить бронь
]
