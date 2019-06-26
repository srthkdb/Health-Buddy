from django.db import models
from django.contrib.auth.models import Permission, User
from Doctor.models import Prescription

# Create your models here.

class bodyVital(models.Model):
    bloodPressure = models.CharField(max_length=50, blank=True)
    weight = models.IntegerField(blank=True)
    height = models.CharField(max_length=10, blank=True)
    sugarLevel = models.CharField(max_length=20, blank=True)
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.id
