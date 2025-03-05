from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reservation
from customers.models import Customer
from tables.models import Table
import datetime

@csrf_exempt
def create_reservation(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer_id")
        table_id = request.POST.get("table_id")
        date = request.POST.get("date")

        customer = get_object_or_404(Customer, id=customer_id)
        table = get_object_or_404(Table, id=table_id)

        # Проверка на наличие брони
        if Reservation.objects.filter(customer=customer, date=date).exists():
            return JsonResponse({"error": "У пользователя уже есть бронь на эту дату"}, status=400)

        if Reservation.objects.filter(table=table, date=date).exists():
            return JsonResponse({"error": "Этот столик уже забронирован на указанную дату"}, status=400)

        reservation = Reservation.objects.create(customer=customer, table=table, date=date)
        return JsonResponse({"id": reservation.id, "status": reservation.status})

def get_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return JsonResponse({
        "id": reservation.id,
        "customer": reservation.customer.name,
        "table": reservation.table.number,
        "date": reservation.date,
        "status": reservation.status
    })

def get_user_reservations(request, user_id):
    reservations = Reservation.objects.filter(customer_id=user_id)
    return JsonResponse(list(reservations.values()), safe=False)

@csrf_exempt
def update_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == "POST":
        status = request.POST.get("status")
        if status in ["pending", "confirmed", "canceled"]:
            reservation.status = status
            reservation.save()
            return JsonResponse({"message": "Статус обновлен", "status": reservation.status})
        else:
            return JsonResponse({"error": "Некорректный статус"}, status=400)

@csrf_exempt
def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.delete()
    return JsonResponse({"message": "Бронь удалена"})
