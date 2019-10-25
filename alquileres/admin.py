from django.contrib import admin

# Register your models here.
from .models import Reservation, City, Property, RentalDate

admin.site.register({Reservation, City, Property, RentalDate})