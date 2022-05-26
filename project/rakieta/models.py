from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128)

class Institution(models.Model):
    CHOICES = [
        ('FUN', 'fundacja'),
        ('ORG', 'organizacja pozarządowa'),
        ('ZBI', 'zbiórka lokalna'),
    ]
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    type = models.CharField(max_length=128, choices=CHOICES, default="FUN")
    categories = models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=24)
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.TextField(max_length=258)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)