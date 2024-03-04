# Django Imports
from django import forms
from django.core.exceptions import ValidationError

# Inside Project Imports
from .models import Task, Category


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description',
                  'priority', 'task_image', 'categories']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "...."}),
            "task_image": forms.FileInput(attrs={"class": "form-control"}),
            "priority": forms.Select(attrs={"class": "form-control"}),
            "categories": forms.SelectMultiple(attrs={"class": "form-control"}),

        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('user')
        del kwargs['user']
        super().__init__(*args, **kwargs)
        self.fields['categories'].queryset = Category.objects.filter(
            user=self.user)


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'description', 'category_image']

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "...."}),
            "category_image": forms.FileInput(attrs={"class": "form-control"}),
        }
