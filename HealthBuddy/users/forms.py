from django import forms
from .models import Type
from django.contrib.auth.models import User
from Patient.models import Patient

#only for patient's registration
class UserForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    isStudent = forms.BooleanField()

#for login
class DefUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class StffPatientRegForm(forms.ModelForm):

    class Meta:
        model = Patient
        exclude = ['prescription', 'user', 'ccUsername', 'program', 'hall', 'room']

class StudPatientRegForm(forms.ModelForm):

    class Meta:
        model = Patient
        exclude = [
            'bloodGroup',
            'ccUsername',
            'prescription',
            'user',
            'program',
            'department',
            'hall',
            'room',
            'gender',
            'hometown',
            'designation',
            'is_dependent',
            'dependentUser',
            'dependentRelation'
        ]
