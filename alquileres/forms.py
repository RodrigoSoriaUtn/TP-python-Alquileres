from django import forms
from bootstrap_datepicker_plus import DatePickerInput
import datetime

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
    start_date = forms.DateField(
        widget=DatePickerInput().start_of('event days')
    )
    end_date = forms.DateField(
        widget=DatePickerInput().end_of('event days')
    )

    def setRentableDays(self, rentalDays) :
        enabledDays = []
        for rentableDay in rentalDays :
            enabledDays.append(rentableDay.__str__())

        datePickerOptions = {
            'format': 'DD/MM/YYYY',
            'minDate': datetime.datetime.today().strftime('%m/%d/%Y'),
            'enabledDays' : enabledDays
        }
        self.start_date.widget.options = datePickerOptions