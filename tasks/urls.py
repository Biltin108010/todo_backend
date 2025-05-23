from django.contrib import admin 
from django.urls import path
from .views import AddTaskView, EditTaskView, DeleteTaskView, SearchTaskView, TaskDetailView
from django.http import HttpResponse
from .views import SecureHelloView

# Your home view
def home(request):
    return HttpResponse("Welcome to the Todo app!")

urlpatterns = [
    path('', home, name='home'),  # This will handle requests to the root URL '/'
    path('admin/', admin.site.urls),  # Add the admin URL for Django admin
    path('tasks/add/', AddTaskView.as_view(), name='task-add'),
    path('tasks/edit/<int:pk>/', EditTaskView.as_view(), name='task-edit'),
    path('tasks/delete/<int:pk>/', DeleteTaskView.as_view(), name='task-delete'),
    path('tasks/search/', SearchTaskView.as_view(), name='task-search'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/', SearchTaskView.as_view(), name='task-list'), 
    path('secure-hello/', SecureHelloView.as_view()),
]
