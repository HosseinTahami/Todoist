# Django Imports

from django.urls import path

# Inside Project Imports

from . import views


app_name = 'account'

urlpatterns = [

    path('profile/<int:user_id>/',
         views.UserProfileView.as_view(), name='user_profile'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),

]
