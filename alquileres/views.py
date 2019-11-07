from datetime import date
from django.http import Http404
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

def viewProperty(request, property_id):
    try:
        prop = Property.objects.get(pk=property_id)
        if (request.method == 'POST') :
            makeReservation(request, prop)
    except Property.DoesNotExist:
        raise Http404("Property does not exist")
    return loadPropertyView(request, prop)

def loadPropertyView(request, prop) :
    rentalDays = RentalDate.objects.filter(property=prop)
    context = {
        'property' : prop,
        'rentableDays' : rentalDays
    }
    return render(request, 'alquileres/viewProperty.html', context)
    
def makeReservation(request, prop) :
    if (request.POST['daysToRent']) : 
        daysIds = request.POST['daysToRent']
        rentalDates = RentalDate.objects.filter(pk__in=daysIds).filter(property__equals=prop)
        
        reservation = Reservation(date.today, prop.daily_price * rentalDates.len())
        reservation.save()

        for rentalDate in rentalDates :
            rentalDate.reservation = reservation
            rentalDate.save()