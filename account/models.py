# Django Imports
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Inside Project Imports
from .managers import CustomUserManager


class User(AbstractBaseUser):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other')
    ]
    email = models.EmailField(unique=True)
    username = models.CharField(
        unique=True, max_length=15, null=True, blank=True)
    phone_number = models.CharField(
        unique=True, max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default=...)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=1, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'username', 'phone_number']

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.email}'
