from django.db import models

class students(models.Model):
    roll = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=200)
    program = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    hall = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)

    def __str__(self):
        return self.name
