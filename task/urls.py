# Django Imports
from django.urls import path

# Inside Project Imports
from . import views

app_name = 'task'

urlpatterns = [
    path('<int:pk>/tasks/', views.TaskView.as_view(), name='tasks'),
    path('<int:pk>/categories/', views.CategoryView.as_view(), name='categories'),
    path('task/update/<int:pk>/', views.UpdateTaskView.as_view(), name='update_task'),
    path('task/detail/<int:pk>/', views.DetailTaskView.as_view(), name='detail_task'),
    path('category/update/<int:pk>/',
         views.UpdateCategoryView.as_view(), name='update_category'),
    path('category/detail/<int:pk>/',
         views.DetailCategoryView.as_view(), name='detail_category'),
    path('task/delete/<int:pk>/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('category/delete/<int:pk>/',
         views.DeleteCategoryView.as_view(), name='delete_category'),

]
