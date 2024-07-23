from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:task_id>/', views.update, name="update"),
    path('update_not_completed/<int:task_id>/', views.update_not_completed, name="update_not_completed"),
    path('delete/<int:task_id>/', views.delete_task, name="delete"),
    path('details/<int:task_id>/', views.details, name="details"),
]

