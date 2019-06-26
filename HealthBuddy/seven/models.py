from django.db import models

# Create your models here.
class Test(models.Model):
    test = models.CharField(max_length=100)


class bodyVital(models.Model):
    bloodPressure = models.CharField(max_length=50, blank=True)
    weight = models.IntegerField(blank=True)
    height = models.CharField(max_length=10, blank=True)
    sugarLevel = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.id
