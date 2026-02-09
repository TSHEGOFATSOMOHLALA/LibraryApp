from django.shortcuts import render
from .models import Bike, Renter, Rental

# Create your views here.

# Home
def home(request):
    return render(request, 'BikeRentalApp/home.html')

# Bike list
def bikelist(request):
    bikes = Bike.objects.all()
    return render(request, 'BikeRentalApp/bikelist.html', {"bikes": bikes})

# Renter list
def renterlist(request):
    renters = Renter.objects.all()
    return render(request, 'BikeRentalApp/renterlist.html', {"renters": renters})

# Rental list
def rentallist(request):
    rentals = Rental.objects.all()
    return render(request, 'BikeRentalApp/rentallist.html', {"rentals": rentals})