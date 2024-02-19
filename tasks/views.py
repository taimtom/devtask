from rest_framework import  permissions,  generics
from .models import Task
from .serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        queryset=Task.objects.all()
        return queryset

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        queryset=Task.objects.all()
        return queryset