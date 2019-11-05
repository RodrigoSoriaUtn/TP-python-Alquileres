from django.contrib import admin

# Register your models here.
from .models import Reservation, City, Property, RentalDate, Host

admin.site.register({Reservation, City, RentalDate, Host})

class hostProperty(admin.ModelAdmin) :

    def get_queryset(self, request) :
        return Property.objects.filter(host=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk :
            obj.host = request.user
        super(hostProperty, self).save_model(request, obj, form, change)

admin.site.register(Property, hostProperty)