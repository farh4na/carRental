# from cProfile import Profile
# from django.core.validators import *
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
# from user.models import Profile 


# Create your models here.
  
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address']

class Car(models.Model):
    CAR_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('hatchback', 'Hatchback'),
    ]

    TRANSMISSION_CHOICES = [
        ('auto', 'Automatic'),
        ('manual', 'Manual'),
    ]

    BRAND_CHOICES = [
        ('proton', 'Proton'),
        ('perodua', 'Perodua'),
        ('honda', 'Honda'),
        ('toyota', 'Toyota'),
    ]

    SEATS_CHOICES = [
        (5, '5'),
        (7, '7'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/')
    car_type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)
    brand = models.CharField(max_length=10, choices=BRAND_CHOICES)
    seats = models.IntegerField(choices=SEATS_CHOICES)
    price_range = models.CharField(max_length=10, choices=[('0-200', '0-200'), ('>200', '>200')])
  
    def __str__(self):
        return self.name
    
class Rental(models.Model):
    location = models.CharField(max_length=100, blank=True)
    pickup_date = models.DateField(blank=True, null=True)
    pickup_time = models.TimeField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    return_time = models.TimeField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)  # Adjust max_length if needed
    
    def __str__(self):
        return f"Rental at {self.location} from {self.pickup_date} to {self.return_date}"