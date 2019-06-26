from django import forms
from Patient.models import Patient


class PatientRegForm(forms.ModelForm):

    class Meta:
        model = Patient
        exclude = ['prescription', 'user']