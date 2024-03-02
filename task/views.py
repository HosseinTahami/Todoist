# Django Imports

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Inside Project Imports

from .models import Category, Task


class TaskView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        tasks = Task.objects.all().filter(user=user)
        return render(request, 'task/tasks.html', {'tasks': tasks})


class CategoryView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        categories = Category.objects.all().filter(user=user)
        return render(request, 'task/categories.html', {'categories': categories})
