from django.shortcuts import render
from .models import Resident, Caretaker, Assistance

def home(request):
    return render(request, "carehome/home.html")

def resident_list(request):
    residents = Resident.objects.all()
    return render(request, "carehome/resident_list.html", {"residents":residents})

def caretaker_list(request):
    caretakers = Caretaker.objects.all()
    return render(request, "carehome/caretaker_list.html", {"caretakers":caretakers})

def assistance_list(request):
    records = Assistance.objects.select_related("resident","caretaker").all()
    return render(request, "carehome/assistance_list.html", {"records":records})