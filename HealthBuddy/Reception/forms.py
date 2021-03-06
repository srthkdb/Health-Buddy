from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['patient_roll', 'doctor', 'brief']


class ApproveForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['doctor', 'brief']