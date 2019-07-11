from django.contrib import admin
from Patient.models import Patient, PatHistory

# Register your models here.
admin.site.register(Patient)
admin.site.register(PatHistory)