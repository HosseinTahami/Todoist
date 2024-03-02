# Django Imports
from django.db import models


# Inside Project Imports
from account.models import User


class Task(models.Model):
    PRIORITY_CRITICAL = "C"
    PRIORITY_MEDIUM = "M"
    PRIORITY_LOW = "L"
    PRIORITY_CHOICES = [
        (PRIORITY_CRITICAL, "Critical"),
        (PRIORITY_MEDIUM, "Medium"),
        (PRIORITY_LOW, "Low")
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    priority = models.CharField(
        max_length=1, choices=PRIORITY_CHOICES, default=PRIORITY_LOW)
