# Django Imports
from django.urls import path

# Inside Project Imports
from . import views

app_name = "account"

urlpatterns = [
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='user_profile'),
]
