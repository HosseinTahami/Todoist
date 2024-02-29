# Django Imports
from django.urls import path

# Inside Project Imports
from . import views

app_name = "core"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
