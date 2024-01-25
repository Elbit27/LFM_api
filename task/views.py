from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from .models import Task
from .permissions import IsOwner, IsOwnerOrAdmin

from like.models import Favorite
from review.serializers import ReviewSerializer
from respond.serializers import RespondSerializer


class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    pagination_class = StandartResultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('title', 'body')
    filterset_fields = ('owner', 'category')

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

    @action(['POST', 'DELETE'], detail=True)
    def favorites(self, request, pk):
        task = self.get_object()
        user = request.user
        favorite = user.favorites.filter(task=task)

        if request.method == 'POST':
            if favorite.exists():
                return Response({'msg': 'Already in Favorites'}, status=400)
            Favorite.objects.create(owner=user, task=task)
            return Response({'msg': 'Added to Favorite'}, status=201)

        if favorite.exists():
            favorite.delete()
            return Response({'msg': 'Deleted from Favorites'}, status=204)
        return Response({'msg': 'Favorite Not Found!'}, status=404)

    # ...api/v1/posts/<id>/
    @action(['GET'], detail=True)
    def reviews(self, request, pk):
        task = self.get_object()
        reviews = task.comments.all()
        serializer = ReviewSerializer(instance=reviews, many=True)
        return Response(serializer.data, status=200)

    # .../api/v1/tasks/pk/...
    @action(['GET'], detail=True)
    def responds(self, request, pk):
        task = self.get_object()
        responds = task.responds.all()
        serializer = RespondSerializer(instance=responds, many=True)
        return Response(serializer.data, status=200)
