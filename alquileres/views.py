from datetime import date
from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Property, Reservation, RentalDate

# Create your views here.

def index(request):
    property_list = Property.objects.all()
    template = loader.get_template('alquileres/index.html')
    context = {
        'property_list' : property_list
    }
    return HttpResponse(template.render(context, request))

def propertyToRent(request, propertyId) :
    prop : Property = Property.objects.get(id=propertyId)
    if (request.method == 'POST') :
        makeReservation(request, prop)

    return loadPropertyView(request, prop)
    
def makeReservation(request, prop) :
    # TODO : Surround by try except block. Ask why.
    if (request.POST['daysToRent']) : 
        daysIds = request.POST['daysToRent']
        rentalDates = RentalDate.objects.filter(pk__in=daysIds).filter(property__equals=prop)
        
        reservation = Reservation(date.today, prop.daily_price * rentalDates.len())
        reservation.save()

        for rentalDate in rentalDates :
            rentalDate.reservation = reservation
            rentalDate.save()

def loadPropertyView(request, prop) :
    # TODO : Change this. Verify with marcus.
    rentalDays = RentalDate.objects.filter(property=prop)
    template = loader.get_template('alquleres/index.html')
    context = {
        'property' : prop,
        'rentableDays' : rentalDays
    }
    return HttpResponse(template.render(context, request))