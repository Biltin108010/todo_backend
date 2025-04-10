from rest_framework import generics, filters
from .models import Task
from .serializers import TaskSerializer
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger(__name__)

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

class SearchTaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        search_query = self.request.query_params.get('search', None)
        logger.info(f"Search query received: {search_query}")  # Log the search query

        queryset = super().get_queryset()

        # If search_query is not empty, apply the search filter
        if search_query:
            logger.info(f"Filtering tasks with search query: {search_query}")
            queryset = queryset.filter(title__icontains=search_query)

        return queryset

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # Allow PATCH for partial updates
    http_method_names = ['get', 'put', 'patch', 'delete']

class SecureHelloView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}!"})
