# Django Imports

from django.contrib import admin

# Inside Project Imports

from . import models

admin.site.register(models.Category)


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ['title', 'user', 'created_at', 'priority']
    list_editable = ['priority']
    list_per_page = 10
    list_filter = ['priority']
    ordering = ['user']
