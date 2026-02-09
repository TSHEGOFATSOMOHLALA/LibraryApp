from django.contrib import admin
from .models import Event, Attendee, Registration
# Register your models here.
# EventApp/admin.py






@admin.register(Event)

class EventAdmin(admin.ModelAdmin):

  pass



@admin.register(Attendee)

class AttendeeAdmin(admin.ModelAdmin):

  pass



@admin.register(Registration)

class RegistrationAdmin(admin.ModelAdmin):

  list_display = ("attendee", "event")

  readonly_fields = ("ticket_price",)