# Django Imports

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Inside Project Imports

from .models import Category, Task
from .forms import CreateTaskForm


class TaskView(LoginRequiredMixin, View):

    template_name = 'task/tasks.html'
    form_class = CreateTaskForm

    def setup(self, request, *args, **kwargs):
        self.user = request.user
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(user=self.user)
        tasks = Task.objects.all().filter(user=self.user)
        return render(request, self.template_name, {'tasks': tasks, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(
            data=request.POST, files=request.FILES, user=self.user)
        if form.is_valid():
            cd = form.cleaned_data
            new_task = form.save(commit=False)
            new_task.user = self.user
            new_task.save()
            messages.success(
                request, 'Task Created Successfully', 'success')
            return redirect('task:tasks', pk=self.user.id)


class CategoryView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        categories = Category.objects.all().filter(user=user)
        return render(request, 'task/categories.html', {'categories': categories})
