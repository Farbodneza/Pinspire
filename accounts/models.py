from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True,null=True)
    profile_picture = models.ImageField(blank=True, null=True)