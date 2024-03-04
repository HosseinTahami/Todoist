# Django Imports

from django.contrib import admin

# Inside Project Imports

from . import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'user', 'created_at', 'priority']
    list_editable = ['priority']
    list_per_page = 10
    list_filter = ['priority']
    ordering = ['user']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'user', 'created_at']
    list_editable = ['user']
    list_filter = ['user']
    ordering = ['user']
    search_fields = ['user']
