from django.db import models

class employee(models.Model):
    name = models.CharField(max_length=50)
    desig = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=10)
    resid = models.CharField(max_length=50)

    def __str__(self):
        return self.name