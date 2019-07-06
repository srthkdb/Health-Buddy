from django import forms
from .models import PatHistory
from Reception.models import Appointment

class PatHistoryForm(forms.ModelForm):

    class Meta:
        model = PatHistory
        fields = ['treatmentFor', 'remarks', 'file']

class AppointmentRequestForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['brief', 'doctor']
