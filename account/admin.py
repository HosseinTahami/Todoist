# Django Imports

from django.contrib import admin

# Inside Project Imports

from .models import User

admin.site.register(User)
