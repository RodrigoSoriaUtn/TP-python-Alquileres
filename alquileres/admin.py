from django.contrib import admin

# Register your models here.
from .models import Reservation, City, Property, RentalDate, Host

admin.site.register({City, Host})

class RentalDateInline(admin.TabularInline) :
    model = RentalDate

class hostProperty(admin.ModelAdmin) :

    inlines = [
        RentalDateInline
    ]

    def get_queryset(self, request) :
        return Property.objects.filter(host=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk :
            obj.host = request.user
        super(hostProperty, self).save_model(request, obj, form, change)

admin.site.register(Property, hostProperty)


class hostRentalDates(admin.ModelAdmin) :
    
    exclude = ['reservation']

    def get_queryset(self, request) : 
        return RentalDate.objects.filter(property__host=request.user)


admin.site.register(RentalDate, hostRentalDates)


class hostReservation(admin.ModelAdmin) :

    def get_queryset(self, request) :
        return Reservation.objects.filter(rentaldate__property__host=request.user)

admin.site.register(Reservation, hostReservation)