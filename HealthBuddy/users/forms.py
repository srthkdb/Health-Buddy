from django import forms
from .models import Type

#this file is for tweaking the default UserForm to remove useless fiels and add new forms.

class UserForm(forms.Form):
    #this tells django is password is a password field
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    options = [
        ('phr', 'Pharmacy'),
        ('rec', 'Reception'),
        ('doc', 'Doctor'),
        ('pat', 'Patient'),
    ]
    user_type = forms.ChoiceField(
        choices = options,
    )
