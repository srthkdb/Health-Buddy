from django.contrib import admin
from Doctor.models import HCDept, Day, Prescription, Doctor

# Register your models here.
admin.site.register(HCDept)
admin.site.register(Day)
admin.site.register(Prescription)
admin.site.register(Doctor)