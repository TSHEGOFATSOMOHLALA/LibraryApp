from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("bikes/", views.bikelist, name="bikelist"),
    path("renters/", views.renterlist, name="renterlist"),
    path("rentals/", views.rentallist, name="rentallist"),
]