from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bloodGroup = models.CharField(max_length=10, blank=True)
    allergies = models.CharField(max_length=500, default='none')
    significantMedicalHistory = models.CharField(max_length=5000, default='none')
    phoneNo = models.CharField(max_length=50)
    emergencyContactName = models.CharField(max_length=50)
    emergencyContactNo = models.CharField(max_length=50)
    emergencyContactRelation = models.CharField(max_length = 20)
    rollNo = models.CharField(max_length=100, primary_key=True)
    is_dependent = models.BooleanField(default=True)
    dependentUser = models.CharField(max_length=25, blank=True)
    dependentRelation = models.CharField(max_length=50, blank=True)
    designation = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)
    ccUsername = models.CharField(max_length=20, blank=True)
    program = models.CharField(max_length=30, blank=True)
    hall = models.CharField(max_length=50, blank=True)
    room = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    hometown = models.CharField(max_length=30, blank=True)
    per_addr = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True)
    height = models.CharField(max_length=20, blank=True)
    weight = models.CharField(max_length=20, blank=True)
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class PatHistory(models.Model):
    treatmentFor = models.CharField(max_length=150)
    remarks = models.TextField(blank=True)
    file = models.FileField(blank=True)
    file_url = models.CharField(max_length=100, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
