from rest_framework.viewsets import ModelViewSet
from .models import Task
from . import serializers
from .permissions import IsOwner, IsOwnerOrAdmin
from rest_framework import permissions


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TaskListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.TaskCreateUpdateSerializer
        elif self.action in ('destroy', 'retrieve'):
            return serializers.TaskDetailSerializer

    def get_permissions(self):
        # удалять может только автор поста или админ
        if self.action == 'destroy':
            return [IsOwnerOrAdmin(), ]
        # обновлять может только автор поста
        elif self.action in ('update', 'partial_update'):
            return [IsOwner(), ]
        # просматривать могут все (list, retrive)
        # создавать может только залогиненный пользователь
        return [permissions.IsAuthenticatedOrReadOnly(), ]

