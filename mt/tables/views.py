from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Table
import datetime

@csrf_exempt
def create_table(request):
    if request.method == "POST":
        number = request.POST.get("number")
        capacity = request.POST.get("capacity")
        table = Table.objects.create(number=number, capacity=capacity)
        return JsonResponse({"id": table.id, "number": table.number})

def table_list(request):
    tables = Table.objects.all()
    return JsonResponse(list(tables.values()), safe=False)

def available_tables(request):
    date = request.GET.get("date")
    if not date:
        return JsonResponse({"error": "Дата не указана"}, status=400)

    booked_tables = Table.objects.filter(reservation__date=date)
    available_tables = Table.objects.exclude(id__in=booked_tables.values_list('id', flat=True))

    return JsonResponse(list(available_tables.values()), safe=False)
