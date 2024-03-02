# Django Imports
from django import forms

# Inside Project Imports
from . import models


class ProfileViewForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ['email', 'first_name',
                  'last_name', 'username', 'date_of_birth']


class UserLoginForm(forms.ModelForm):

    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "*****"}))

    class Meta:
        model = models.User
        fields = ['email', 'password', 'confirm_password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'mail@email.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*****'})
        }
