from django.db import models
from django.contrib.auth.models import Permission, User 

#Table to store Medicines with attributes name and quantity
# class Medicine(models.Model):
#     name = models.CharField(max_length=500)
#     quantity = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name


#Tests to be performed in Room no. 7
# class Test(models.Model):
#     test = models.CharField(max_length=100)


#Days when the doctor is available
# class Day(models.Model):
#     day = models.CharField(max_length=10)

#     def __str__(self):
#         return self.day

#Department in HC
# class HCDept(models.Model):
#     deptName = models.CharField(max_length=50)

#     def __str__(self):
#         return self.deptName

#User type = Doctor
# class Doctor(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     department = models.ForeignKey(HCDept, on_delete=models.CASCADE)
#     roomNo = models.CharField(max_length=15)
#     visitDays = models.ForeignKey(Day, on_delete=models.CASCADE)
#     timings = models.CharField(max_length=500)


# class Prescription(models.Model):
#     date = models.DateTimeField()
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     #patient's details is in patient's model
#     medicines = models.ForeignKey(Medicine, on_delete=models.CASCADE)
#     remarks = models.TextField()
#     tests = models.ForeignKey(Test, on_delete=models.CASCADE)


# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     bloodGroup = models.CharField(max_length=10)
#     drugAllergies = models.CharField(max_length=500)
#     significantMedicalHistory = models.CharField(max_length=5000)
#     phoneNo = models.CharField(max_length=15)
#     emergencyContactName = models.CharField(max_length=50)
#     emergencyContactNo = models.CharField(max_length=15)
#     rollNo = models.CharField(max_length=15)
#     dependentName = models.CharField(max_length=50)
#     dependentRelation = models.CharField(max_length=15)
#     designation = models.CharField(max_length=15)
#     department = models.CharField(max_length=15)
#     id = models.CharField(max_length=10, primary_key=True)
#     prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.id



# class bodyVital(models.Model):
#     bloodPressure = models.CharField(max_length=50)
#     weight = models.IntegerField()
#     height = models.CharField(max_length=10)
#     sugarLevel = models.CharField(max_length=20)
#     prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE)
    


