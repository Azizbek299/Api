from django.db import models
from django.contrib.auth.models import User


class Boglanish(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bog')
    phone = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    objects = None
    phone_number = models.CharField(max_length=50)
    date_phone_number = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number

