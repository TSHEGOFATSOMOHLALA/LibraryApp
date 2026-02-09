from django.contrib import admin
from .models import Bike, Renter, Rental
@admin.register(Bike)

class BikeAdmin(admin.ModelAdmin):
    list_display = ("bike_type", "color")
    list_filter = ("bike_type",)
    search_fields = ("color",)

@admin.register(Renter)
class RenterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "vip_num")
    search_fields = ("first_name", "last_name", "phone")

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ("renter", "bike", "date", "price") # show price in list list_filter = ("date", "bike bike_type")
    search_fields = ("renter first_name", "renter last_name")
    # Step 1: make price read-only
    readonly_fields = ("price",)

# Step 2: recalc price when saving in admin
    def save_model(self, request, obj, form, change):
        obj.calc_price() # ensures price always recalculates
        super().save_model(request, obj, form, change)
