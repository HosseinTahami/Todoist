# Django Imports

from django.contrib import admin

# Inside Project Imports

from . import models


admin.site.register(models.Category)

admin.site.register(models.Task)
