from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class AppUser(AbstractUser):
    phone = models.CharField(max_length=100, null=False)
    telegram = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
