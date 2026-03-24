from django.urls import path

from . import views



urlpatterns = [

  path("", views.home, name="event_home"),

  path("events/", views.event_list, name="event_list"),

  path("attendees/", views.attendee_list, name="attendee_list"),

  path("registrations/", views.registration_list, name="registration_list"),

]