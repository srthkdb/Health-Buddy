from django import forms
from .models import PatHistory

class PatHistoryForm(forms.ModelForm):

    class Meta:
        model = PatHistory
        fields = ['treatmentFor', 'remarks', 'file']