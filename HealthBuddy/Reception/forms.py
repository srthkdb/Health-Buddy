from django import forms
from .models import Appointment

class AppointmentForm(form.ModelForm):

    class Meta:
        model = Appointment
        fields = ['patient_roll', 'doctor', 'brief']
