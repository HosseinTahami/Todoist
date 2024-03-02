# Django Imports

from django.contrib import admin

# Inside Project Imports

from . import models


admin.site.register(models.Task)
admin.site.register(models.Category)
