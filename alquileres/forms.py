from django import forms
import datetime

from alquileres.models import City


class ReservationForm(forms.Form):

    name = forms.CharField(label='', max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Name', 
                'class' : 'form-control font-weight-bold'}))
    surname = forms.CharField(label='', max_length=30, 
        widget=forms.TextInput(
            attrs={'placeholder': 'surName', 
                'class' : 'form-control font-weight-bold'}))
    email = forms.EmailField(label='', max_length=50, 
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail', 
                'class' : 'form-control font-weight-bold'}))

class PropertyFilterForm (forms.Form):
    city = forms.ModelChoiceField(required=False, label=(''), queryset=City.objects.all(), empty_label="Choose a city")
    min_pax = forms.IntegerField(required=False, label=(''), widget=forms.NumberInput(
        attrs={'placeholder': 'Min Pax',
               'class': 'form-control font-weight-bold',
               'style': 'width: 30%;'}))
