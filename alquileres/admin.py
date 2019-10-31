from django.contrib import admin

# Register your models here.
from .models import Reservation, City, Property, RentalDate

admin.site.register({Reservation, City, RentalDate})

class hostProperty(admin.ModelAdmin) :
    fields = [ ('title', 'host'), 
        'description', 
        'city', 'address', 
        'max_pax', 'daily_price', 
        'image']

admin.site.register(Property, hostProperty)