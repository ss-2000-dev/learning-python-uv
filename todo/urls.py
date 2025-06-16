from django.urls import path
from .views import todo_list, delete_task, edit_task

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
]