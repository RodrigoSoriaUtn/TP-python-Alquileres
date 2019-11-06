from django.http import Http404
from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Property

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
        property = Property.objects.get(pk=property_id)
    except Property.DoesNotExist:
        raise Http404("Property does not exist")
    return render(request, 'alquileres/viewProperty.html', {'property': property})