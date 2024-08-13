from rest_framework.serializers import ModelSerializer
from .models import project, task, subtask

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'


class SubtaskSerializer(ModelSerializer):
    class Meta:
        model = subtask
        fields = '__all__'