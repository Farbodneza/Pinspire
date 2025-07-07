from django.db import models
from taggit.managers import TaggableManager
from accounts.models import CustomUser


class Pin(models.Model):
    owner = models.ForeignKey(CustomUser,related_name='user_pin', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/pins')
    title = models.TextField(max_length=150)
    description = models.TextField()
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

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
    pins = models.ManyToManyField(Pin, related_name='boards', blank=True)
    

class Likes(models.Model):
    user = models.OneToOneField(CustomUser, related_name="user_likes", on_delete=models.CASCADE)
    pins = models.OneToOneField(Pin, related_name="pin_likes", on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now=True)


class Wishlist(models.Model):
    user = models.OneToOneField(CustomUser, related_name="user_wishlist", on_delete=models.CASCADE)
    pins = models.OneToOneField(Pin, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'pins')