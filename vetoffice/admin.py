from django.contrib import admin
from .models import Patient, Owner

admin.site.register(Patient)
admin.site.register(Owner)