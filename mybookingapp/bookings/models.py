from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)


def __str__(self):
    return self.username
