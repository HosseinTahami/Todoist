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
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(
        max_length=1, choices=PRIORITY_CHOICES, default=PRIORITY_LOW)
    task_image = models.ImageField(
        default='tasks/task/images/default.png', upload_to='tasks/task/images/')
    categories = models.ManyToManyField(
        'Category', related_name='tasks')

    def __str__(self):
        return self.title


class Category(models.Model):
    user = user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='categories')
    title = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    category_image = models.ImageField(
        default='tasks/category/images/default.jpg', upload_to='tasks/category/images/')

    def __str__(self):
        return self.title
