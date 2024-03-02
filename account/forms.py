# Django Imports
from django import forms

# Inside Project Imports
from . import models


class ProfileViewForm(forms.Form):

    class Meta:
        model = models.User
        fields = ['email', 'first_name',
                  'last_name', 'username', 'date_of_birth']
