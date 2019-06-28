from django.db import models
from django.contrib.auth.models import Permission, User 

class Type(models.Model):
    options = [
        ('phr', 'Pharmacy'),
        ('rec', 'Reception'),
        ('doc', 'Doctor'),
        ('pat', 'Patient'),
    ]
    types = models.CharField(
        max_length = 3,
        choices = options,
        default = 'pat',
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.user.username


