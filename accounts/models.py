# Django Imports

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Inside Project Imports

from .manager import UserManager


class User(AbstractBaseUser):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    profile_img = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name} | {self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
