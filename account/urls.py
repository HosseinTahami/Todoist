# Django Imports
from django.urls import path

# Inside Project Imports
from . import views

app_name = "account"

urlpatterns = [
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
