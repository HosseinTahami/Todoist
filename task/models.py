# Django Imports

from django.db import models

# Inside Project Import

from account.models import User


class Task(models.Model):

    PRIORITY_CHOICES = [
        ('C', 'Critical'),
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    associated_file = models.FileField(
        blank=True, null=True, upload_to='Tasks/file/')
    image = models.ImageField(
        default='tasks/image/default.jpg', upload_to='tasks/image/')
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} | {self.user.first_name}'
