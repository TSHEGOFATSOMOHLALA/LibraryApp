import os
import django
import datetime

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from BikeRentalApp.models import Bike, Renter, Rental

def run():
    # Clear old data (optional)
    Bike.objects.all().delete()
    Renter.objects.all().delete()
    Rental.objects.all().delete()

    # Add Bikes
    b1 = Bike.objects.create(bike_type=Bike.STANDARD, color="Red")
    b2 = Bike.objects.create(bike_type=Bike.TANDEM, color="Blue")
    b3 = Bike.objects.create(bike_type=Bike.ELECTRIC, color="Black")
    b4 = Bike.objects.create(bike_type=Bike.STANDARD, color="Green")

    # Add Renters
    r1 = Renter.objects.create(first_name="Alice", last_name="Smith", phone="0123456789", vip_num=1)
    r2 = Renter.objects.create(first_name="Bob", last_name="Johnson", phone="0987654321", vip_num=0)
    r3 = Renter.objects.create(first_name="Charlie", last_name="Brown", phone="0112233445", vip_num=2)

    # Add Rentals
    Rental.objects.create(bike=b1, renter=r1, date=datetime.date.today())
    Rental.objects.create(bike=b2, renter=r2, date=datetime.date.today())
    Rental.objects.create(bike=b3, renter=r3, date=datetime.date.today())

    print("✅ Database populated with sample data!")

if __name__ == "__main__":
    run()
