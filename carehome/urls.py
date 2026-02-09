from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("resident/", views.resident_list, name="resident_list"),
    path("caretaker/", views.caretaker_list, name="caretaker_list"),
    path("assistance/", views.assistance_list, name="assistance_list"),
]