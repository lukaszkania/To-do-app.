from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from to_do.models import Task


class TaskModelViewApiSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by('pk')
