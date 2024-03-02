# Django Imports
from django.urls import path

# Inside Project Imports
from . import views

app_name = 'task'

urlpatterns = [
    path('<int:pk>/tasks/', views.TaskView.as_view(), name='tasks'),
    path('<int:pk>/categories/', views.CategoryView.as_view(), name='categories'),
]
