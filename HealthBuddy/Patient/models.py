from django.db import models
from django.contrib.auth.models import Permission, User
from Doctor.models import Prescription

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bloodGroup = models.CharField(max_length=10, blank=True)
    drugAllergies = models.CharField(max_length=500, default='none')
    significantMedicalHistory = models.CharField(max_length=5000, default='none')
    phoneNo = models.CharField(max_length=15)
    emergencyContactName = models.CharField(max_length=50)
    emergencyContactNo = models.CharField(max_length=15)
    emergencyContactRelation = models.CharField(max_length = 20)
    rollNo = models.CharField(max_length=15, primary_key=True)
    is_dependent = models.BooleanField(default=True)
    dependentUser = models.CharField(max_length=25, blank=True)
    dependentRelation = models.CharField(max_length=15, blank=True)
    designation = models.CharField(max_length=15, blank=True)
    department = models.CharField(max_length=15, blank=True)
    prescription = models.ManyToManyField(Prescription, blank=True)

    def __str__(self):
        return self.user.username
