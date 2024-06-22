from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class AppUser(AbstractUser):
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
