# Django Imports

from django import forms
from django.core.exceptions import ValidationError

# Inside Project Imports

from .models import User


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'profile_img', 'phone_number',
                  'email', 'username', 'birth_date',
                  'gender',]

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'phone_number': forms.NumberInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'profile_img': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'birth_date': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("This email is already registered..!")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("This Username is already taken..!")

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise ValidationError(
                "An account exists with this phone number..!")


class UserRegisterForm(forms.Form):

    first_name = forms.CharField(
        label='First Name:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'John'
            }
        )
    )

    last_name = forms.CharField(
        label='Last Name:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Doe'
            }
        )
    )

    email = forms.EmailField(
        label='Email:',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'JohnDoe@email.com'
            }
        )
    )

    password = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '*******'
            }
        )
    )

    confirm_password = forms.CharField(
        label='Confirm Password:',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '*******'
            }
        )
    )

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password and confirm_password and (password != confirm_password):
            return ValidationError("Passwords do not match..!")
        return password
