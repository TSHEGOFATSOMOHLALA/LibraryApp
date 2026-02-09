from django.shortcuts import render
from .models import Event, Attendee, Registration
# Create your views here.

def home(request):
    return render (request,'EventApp/home.html')

def event_list(request):
    events = Event.objects.all()
    return render (  request,'EventApp/event_list.html', {'events':events})

def attendee_list(request):
    attendees = Attendee.objects.all()
    return render (request , 'EventApp/attendee_list.html', {'attendees': attendees})

def registration_list(request):
     registrations = Registration.objects.all()
     return render (request ,  'EventApp/registration_list.html', {'registrations':registrations })

