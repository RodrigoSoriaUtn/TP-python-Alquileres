from django import forms
from bootstrap_datepicker_plus import DatePickerInput
import datetime

class ReservationForm(forms.Form):

    datePickerOptions = {
        'format': 'DD/MM/YYYY',
        'minDate': datetime.datetime.today().strftime('%m/%d/%Y'),
    }

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
    start_date = forms.DateField(
        widget=DatePickerInput(options=datePickerOptions).start_of('event days')
    )
    end_date = forms.DateField(
        widget=DatePickerInput(options=datePickerOptions).end_of('event days')
    )