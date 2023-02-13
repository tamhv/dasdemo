from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    myfield = models.CharField(max_length=200, null=True, blank=True)
    pass
