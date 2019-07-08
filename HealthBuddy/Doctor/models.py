from django.db import models
from django.contrib.auth.models import Permission, User
from seven.models import TestList, bodyVital
from Patient.models import Patient
# from Reception.models import Appointment

# Create your models here.
class HCDept(models.Model):
    deptName = models.CharField(max_length=50)

    def __str__(self):
        return self.deptName

class Day(models.Model):
    day = models.CharField(max_length=10)

    def __str__(self):
        return self.day

# class DayAndTime(models.Model):
#     visitDay = models.ManyToManyField(Day)
#     start_time = models.TimeField("Start Time")
#     end_time = models.TimeField("End Time")

class Timing(models.Model):
    timing = models.CharField(max_length= 10)

    def __str__(self):
        return self.timing

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    department = models.ForeignKey(HCDept, on_delete=models.CASCADE)
    roomNo = models.CharField(max_length=15)
    visitDays = models.ManyToManyField(Day)
    timings = models.ForeignKey(Timing, on_delete = models.CASCADE)
#     visit_day_time = models.ForeignKey(DayAndTime, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username


class Prescription(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor")
    treatmentFor = models.TextField(blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    remarks = models.TextField(blank=True)
    tests = models.ManyToManyField(TestList, blank=True)
    roomNo7 = models.TextField(blank=True)
    med_added = models.BooleanField(default=False)

    def __str__(self):
        return self.treatmentFor


class PresMedicine(models.Model):
    medicine = models.CharField(max_length=100)
    BefOrAft = [
        ('b', 'Before meal'),
        ('a', 'After meal'),
        ('n', 'Night')
    ]
    times_a_day = models.PositiveIntegerField()
    no_of_days = models.PositiveIntegerField()
    when_to_take = models.CharField(
        choices= BefOrAft,
        max_length=1,
        default='a'
    )
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)

    def __str__(self):
        return self.medicine

class References(models.Model):
    from_doc = models.ForeignKey(Doctor, related_name="from_doc", on_delete=models.CASCADE)
    to_doc = models.ForeignKey(Doctor, related_name="to_doc", on_delete=models.CASCADE)
    remarks_from_doc = models.TextField(blank=True)
    remarks_to_doc = models.TextField(blank=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)

    def __str__(self):
        return self.to_doc.user.first_name
