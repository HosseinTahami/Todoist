# Django Imports

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Inside Project Imports

from .models import Category, Task
from .forms import TaskForm, CategoryForm


class TaskView(LoginRequiredMixin, View):

    template_name = 'task/tasks.html'
    form_class = TaskForm

    def setup(self, request, *args, **kwargs):
        self.user = request.user
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if self.user.is_authenticated and self.user.id != kwargs['pk']:
            messages.warning(
                request, 'Do not have access to other accounts tasks..!', 'secondary')
            return redirect('task:tasks', self.user.id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(user=self.user)
        tasks = Task.objects.all().filter(user=self.user)
        return render(request, self.template_name, {'tasks': tasks, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(
            data=request.POST, files=request.FILES, user=self.user)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = self.user
            new_task.save()
            messages.success(
                request, 'Task Created Successfully', 'success')
        return redirect('task:tasks', pk=self.user.id)


class CategoryView(LoginRequiredMixin, View):

    template_name = 'task/categories.html'
    form_class = CategoryForm

    def setup(self, request, *args, **kwargs):
        self.user = request.user
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if self.user.is_authenticated and kwargs['pk'] != self.user.id:
            messages.warning(
                request, 'Do not have access to other accounts categories..!', 'secondary')
            return redirect('task:tasks', self.user.id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        categories = Category.objects.all().filter(user=self.user)
        return render(request, self.template_name, {'categories': categories, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(files=request.FILES, data=request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.user = self.user
            new_category.save()
            messages.success(
                request, "Category Created Successfully..!", 'success')
        return redirect('task:categories', self.user.id)


class UpdateTaskView(View):

    template_name = 'task/update_task.html'
    form_class = TaskForm

    def setup(self, request, *args, **kwargs):
        self.old_task = get_object_or_404(Task, pk=kwargs['pk'])
        self.user = request.user
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if self.user != self.old_task.user:
            messages.error(
                request, 'This task does not belong to you..!', 'danger')
            return redirect('task:tasks', self.user.id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=self.old_task, user=self.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(instance=self.old_task,
                               files=request.FILES, data=request.POST, user=self.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated Successfully !', 'success')
            return redirect('task:tasks', self.user.id)


class DetailTaskView(LoginRequiredMixin, View):

    template_name = 'task/detail_task.html'

    def setup(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=kwargs['pk'])
        self.user = request.user
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if self.user.is_authenticated and self.task.user != self.user:
            messages.error(
                request, 'This task belongs to someone else..!', 'danger')
            return redirect('task:tasks', self.user.id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'task': self.task})
