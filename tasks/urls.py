from django.urls import path
from .views import AddTaskView, EditTaskView, DeleteTaskView, SearchTaskView, TaskDetailView

urlpatterns = [
    path('tasks/add/', AddTaskView.as_view(), name='task-add'),
    path('tasks/edit/<int:pk>/', EditTaskView.as_view(), name='task-edit'),
    path('tasks/delete/<int:pk>/', DeleteTaskView.as_view(), name='task-delete'),
    path('tasks/search/', SearchTaskView.as_view(), name='task-search'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/', SearchTaskView.as_view(), name='task-list'), 
]
