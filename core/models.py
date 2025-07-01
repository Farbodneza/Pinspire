from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True,null=True)
    profile_picture = models.ImageField(blank=True, null=True)


class Pin(models.Model):
    owner = models.ForeignKey(CustomUser,related_name='user_pin', on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.TextField(max_length=150)
    description = models.TextField()
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)


class Board(models.Model):
    VISIBILITY_CHOICES = [
        ('private', 'Private'),
        ('public', 'Public')
    ]
    name = models.CharField(max_length=150)
    description = models.TextField()
    visibility = models.CharField(
        choices=VISIBILITY_CHOICES,
        default='Private'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owner_board')
    pins = models.ManyToManyField(Pin, related_name='boards', blank=True, related_name='pins_board')
    

