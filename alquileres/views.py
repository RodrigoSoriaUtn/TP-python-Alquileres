from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Property

# Create your views here.

def index(request):
    property_list = Property.objects[:5]
    template = loader.get_template('alquileres/index.html')
    context = {
        'property_list' : property_list
    }
    return HttpResponse(template.render(context, request))