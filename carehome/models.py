from django.db import models
import datetime

# Shift-based prices
DAY_PRICE = 200.00
NIGHT_PRICE = 300.00
BOTH_PRICE = 450.00

class Resident(models.Model):
    resident_code = models.CharField(max_length=10, primary_key=True)
    resident_name = models.CharField(max_length=50)
    resident_surname = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.resident_name} {self.resident_surname}"

class Caretaker(models.Model):
    DAY = "DAY"
    NIGHT = "NIGHT"
    BOTH = "BOTH"
    
    SHIFT_CHOICES = [
        (DAY, "Day Shift"),
        (NIGHT, "Night Shift"),
        (BOTH, "Day & Night Shift"),
    ]
    
    caretaker_code = models.CharField(max_length=10, primary_key=True)
    caretaker_name = models.CharField(max_length=50)
    caretaker_surname = models.CharField(max_length=50)
    caretaker_cell = models.CharField(max_length=15)
    shift_type = models.CharField(max_length=10, choices=SHIFT_CHOICES,
    default=DAY)
    
    def __str__(self):
        return f"{self.caretaker_name} {self.caretaker_surname} ({self.shift_type})"

class Assistance(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    caretaker = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    price = models.FloatField(default=0.0)
   
    def calc_price(self):
        """Determine the price based on caretaker shift type."""
        if self.caretaker.shift_type == Caretaker.DAY:
            self.price = DAY_PRICE
        elif self.caretaker.shift_type == Caretaker.NIGHT:
            self.price = NIGHT_PRICE
        elif self.caretaker.shift_type == Caretaker.BOTH:
            self.price = BOTH_PRICE
        return self.price
        
        def save(self, *args, **kwargs):
            # Always recalculate price before saving
            self.calc_price()
            super().save(*args, **kwargs)
        def __str__(self):
            return f"{self.resident} assisted by {self.caretaker} on {self.date} at {self.price}"