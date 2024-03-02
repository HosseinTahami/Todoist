# Django Imports
from django import forms

# Inside Project Imports
from . import models


class ProfileViewForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ['email', 'first_name',
                  'last_name', 'username', 'date_of_birth']


class UserRegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "*****"}))

    class Meta:
        model = models.User
        fields = ['first_name', 'last_name',
                  'email', 'password', 'confirm_password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'JohnDoe@email.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*****'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}),
        }


class UserLoginForm(forms.Form):
    authenticator = forms.CharField(label='Email or Username', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'JohnDoe or JohnDoe@email.com'}))
    password = forms.CharField(label='Email or Username', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': '********'}))
