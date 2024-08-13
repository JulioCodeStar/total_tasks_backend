from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer, TaskSerializer, SubtaskSerializer
from .models import project, task, subtask

# Create your views here.
class ProjectViewSet(ModelViewSet):
    queryset = project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(ModelViewSet):
    queryset = task.objects.all()
    serializer_class = TaskSerializer


class SubtaskViewSet(ModelViewSet):
    queryset = subtask.objects.all()
    serializer_class = SubtaskSerializer