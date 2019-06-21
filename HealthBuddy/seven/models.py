from django.db import models
from django.contrib.auth.models import Permission, User
from Doctor.models import Prescription

# Create your models here.

class bodyVital(models.Model):
    bloodPressure = models.CharField(max_length=50)
    weight = models.IntegerField()
    height = models.CharField(max_length=10)
    sugarLevel = models.CharField(max_length=20)
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE)

