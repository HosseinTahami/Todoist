# Django Imports
from django import forms

# Inside Project Imports
from .models import Task, Category


class CreateTaskForm(forms.ModelForm):

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
        user = kwargs['user']
        del kwargs['user']
        super().__init__(*args, **kwargs)
        self.fields['categories'].queryset = Category.objects.filter(user=user)
