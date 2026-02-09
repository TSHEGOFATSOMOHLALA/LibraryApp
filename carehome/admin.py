from django.contrib import admin
from .models import Resident, Caretaker, Assistance


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ("resident_code", "resident_name", "resident_surname")
    search_fields = ("resident_name", "resident_surname", "resident_code")

@admin.register(Caretaker)
class CaretakerAdmin(admin.ModelAdmin):
    list_display = ("caretaker_code", "caretaker_name",
    "caretaker_surname", "shift_type", "caretaker_cell")
    list_filter = ("shift_type",)
    search_fields = ("caretaker_name", "caretaker_surname",
    "caretaker_code", "caretaker_cell")

@admin.register(Assistance)
class AssistanceAdmin(admin.ModelAdmin):
    list_display = ("resident", "caretaker", "date", "price")
    list_filter = ("date", "caretaker__shift_type")
    search_fields = ("resident__resident_name",
    "resident__resident_surname", "caretaker__caretaker_name")
    # Price is read-only because it is auto-calculated
    readonly_fields = ("price",)