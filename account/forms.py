# Django Imports

from django import forms

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
