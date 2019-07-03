from django.db import models

class TestList(models.Model):
    test = models.CharField(max_length=100)
    
    def __str__(self):
        return self.test

class bodyVital(models.Model):
    testName = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.testName

