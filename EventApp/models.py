from django.db import models
import datetime
# Create your models here.

# Base constants for event types

CONF_BASE = 6000.00

SEM_BASE = 2000.00

WORK_BASE = 5000.00


class Event(models.Model):

   WORKSHOP = "WS"

   SEMINAR = "SE"

   CONFERENCE = "CO"
   GUEST = "GU"

   EVENT_TYPE_CHOICES = [
       (WORKSHOP , "Workshop"),
       (SEMINAR , "Seminar"),
       (GUEST , "Guest"),
       (CONFERENCE , "Conference"),

    ]

   name = models.CharField(max_length=100)
   event_type = models.CharField(max_length=2, choices=EVENT_TYPE_CHOICES, default=WORKSHOP)
   event_date = models.DateField()

   def __str__(self):
        return f"{self.get_event_type_display()}: {self.name} on {self.event_date}"


class Attendee(models.Model):

    STUDENT = "ST"

    STAFF = "SF"

    GUEST = "GU"

    ATTENDEE_TYPE_CHOICES = [
       (STUDENT , "Student"),
       (STAFF , "Staff"),
       (GUEST , "Guest"),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=45)
    attendee_type = models.CharField(max_length=2, choices= ATTENDEE_TYPE_CHOICES, default=STUDENT)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_attendee_type_display()}"

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee =  models.ForeignKey(Attendee, on_delete=models.CASCADE)
    registration_date = models.DateField(default = datetime.date.today)
    ticket_price = models.FloatField(default = 0.0)

    def calc_ticket_price(self):
        if self.event.event_type == Event.WORKSHOP:
            base = WORK_BASE
        elif self.event.event_type == Event.SEMINAR:
            base = SEM_BASE
        elif self.event.event_type == Event.CONFERENCE:
            base = CONF_BASE
        else:
            base = self.event.base_price or 0.0

        if self.attendee.attendee_type == Attendee.STUDENT:
            fin_price = base * 0.5
        elif self.attendee.attendee_type == Attendee.STAFF:
            fin_price = base* 0.25
        else:
            fin_price = base

        self.ticket_price = fin_price
        return self.ticket_price

    def save(self, *args, **kwargs):
        self.ticket_price = self.calc_ticket_price()
        super().save(*args, **kwargs)

    def __str__(self):
         cost_str = f"R {self.ticket_price:.2f}"
         return f"{self.attendee.first_name} {self.attendee.last_name} registered for {self.event.name} on {self.registration_date} with a cost of {cost_str}"







