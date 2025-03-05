from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Customer

def get_customers(request):
    customers = list(Customer.objects.values())
    return JsonResponse(customers, safe=False)

def get_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    return JsonResponse({"id": customer.id, "name": customer.name, "phone": customer.phone})

def create_customer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        customer = Customer.objects.create(name=name, phone=phone)
        return JsonResponse({"id": customer.id, "name": customer.name, "phone": customer.phone})

# Create your views here.
