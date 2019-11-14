import datetime
from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from .forms import ReservationForm
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
    reservationForm = ReservationForm()
    try:
        prop = get_object_or_404(Property, pk=property_id)
        if (request.method == 'POST') :
            reservationForm = ReservationForm(request.POST)

            if reservationForm.is_valid() :
                reservation = makeReservation(request, reservationForm, prop)
                reservationForm = ReservationForm()
                return loadPropertyView(request, prop, reservationForm, reservation.pk)

    except Exception as inst :
       reservationForm.add_error(None, inst)

    return loadPropertyView(request, prop, reservationForm)

def loadPropertyView(request, prop, resForm, reservationID=None) :
    rentalDays = RentalDate.objects.filter(property=prop)
    context = {
        'property' : prop,
        'rentableDays' : rentalDays,
        'reservationForm' : resForm,
        'reservationId' : reservationID
    }
    return render(request, 'alquileres/viewProperty.html', context)

def makeReservation(request, reservationForm, prop) :
        
    name = reservationForm.cleaned_data["name"]
    surname = reservationForm.cleaned_data['surname']
    email = reservationForm.cleaned_data['email']
    if ( not request.POST.getlist('chosenDays') ) :
        raise Exception('You must choose at least one day to reserve ') 
    
    rentalDates = RentalDate.objects.filter(pk__in=request.POST.getlist('chosenDays'))
    validateRentalDates(rentalDates)

    reservation = Reservation()
    reservation.name = name
    reservation.surname = surname
    reservation.email = email
    reservation.created_date = datetime.date.today 
    total = prop.daily_price * rentalDates.count()
    reservation.total_price = total
    reservation.save()

    for rentalDate in rentalDates :
        rentalDate.reservation = reservation
        rentalDate.save()

    return reservation

def validateRentalDates(rentalDates) :
    for rentalDate in rentalDates :
        if rentalDate.reservation :
            raise Exception('The dates selected are not available, please choose others ')