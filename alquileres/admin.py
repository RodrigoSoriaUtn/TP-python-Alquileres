from django.contrib import admin

# Register your models here.
from .models import Reservation, City, Property, RentalDate, Host

admin.site.register({City, Host})

class RentalDateInline(admin.TabularInline) :
    model = RentalDate
    exclude = ['reservation']

class hostProperty(admin.ModelAdmin) :

    inlines = [
        RentalDateInline
    ]

    def get_exclude(self, request, obj) :
        if (not request.user.is_superuser) :
            return ['host'] 
        else :
            return []

    def get_queryset(self, request) :
        if (not request.user.is_superuser) :
            return Property.objects.filter(host=request.user)
        else :
            return Property.objects.all()

    def save_model(self, request, obj, form, change):
        if (not obj.pk and not request.user.is_superuser ) :
            obj.host = Host.objects.get(pk=request.user) 
        super(hostProperty, self).save_model(request, obj, form, change)

admin.site.register(Property, hostProperty)

class hostReservation(admin.ModelAdmin) :

    def get_queryset(self, request) :
        if (not request.user.is_superuser) :
            return Reservation.objects.filter(rentaldate__property__host=request.user)
        else :
            return Reservation.objects.all()

admin.site.register(Reservation, hostReservation)