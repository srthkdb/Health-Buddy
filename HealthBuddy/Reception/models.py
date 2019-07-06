from django.db import models
from django.contrib.auth.models import Permission, User
from Patient.models import Patient
from Doctor.models import Doctor, Prescription

# Create your models here.
class Reception(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor", blank=True)
    dateNtime = models.DateTimeField(auto_now_add=True)
    # time = models.
    brief = models.TextField(blank=True)                 #treatment for
    reqApproval = models.BooleanField(default=False)     #request approved or not
    status = models.BooleanField(default=False)          #completed = True, pending = false
    doc_ref = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doc_ref", blank=True)
    refer_remarks = models.TextField(blank=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    # is_referred = models.BooleanField(default=False)
    def __str__(self):
        return (self.patient.user.username, self.doctor.user.username)

class ReferredAppointment(models.Model):
    prev_app = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="prev_app")
    new_app = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="new_app")
