from rest_framework import generics, filters
from .models import Task
from .serializers import TaskSerializer

# Add a new Task
class AddTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Edit an existing Task
class EditTaskView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Delete a Task
class DeleteTaskView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Search for Tasks
class SearchTaskView(generics.ListCreateAPIView):  # ✅ Supports GET & POST
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # Allow PATCH for partial updates
    http_method_names = ['get', 'put', 'patch', 'delete']

