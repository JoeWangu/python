from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=50, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')])
    address = models.TextField()

    def __str__(self):
        return self.username
