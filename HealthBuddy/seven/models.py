from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.
class Test(models.Model):
    test = models.CharField(max_length=100)


class bodyVital(models.Model):
    bloodPressure = models.CharField(max_length=50)
    weight = models.IntegerField()
    height = models.CharField(max_length=10)
    sugarLevel = models.CharField(max_length=20)
    

