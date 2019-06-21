from django.db import models
from django.contrib.auth.models import Permission, User
from Doctor.models import Prescription

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bloodGroup = models.CharField(max_length=10)
    drugAllergies = models.CharField(max_length=500)
    significantMedicalHistory = models.CharField(max_length=5000)
    phoneNo = models.CharField(max_length=15)
    emergencyContactName = models.CharField(max_length=50)
    emergencyContactNo = models.CharField(max_length=15)
    emergencyContactRelation = models.CharField(max_length = 20)
    rollNo = models.CharField(max_length=15)
    dependentName = models.CharField(max_length=50)
    dependentRelation = models.CharField(max_length=15)
    designation = models.CharField(max_length=15)
    department = models.CharField(max_length=15)
    id = models.CharField(max_length=10, primary_key=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
