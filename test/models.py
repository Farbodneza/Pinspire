from django.db import models
from accounts.models import CustomUser
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    customer_name = models.CharField(max_length=150, unique=True)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now=True)