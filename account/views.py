from dj_rest_auth.views import LogoutView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from django.contrib.auth.models import User
from rest_framework import permissions, generics
from . import serializers
from like.serializers import FavoriteSerializer


class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserListSerializer
        return serializers.UserDetailSerializer

    @action(['GET'], detail=False)
    def favorites(self, request):
        user = request.user
        favorites = user.favorites.all()
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=200)


# Now we need to create view, that registers the user
class UserRegisterView(generics.CreateAPIView):
    serializer_class = serializers.UserRegisterSerializer

# Это кастомизатор для модуля logout. Мы просто устанавливаем пермишенсы
class CastomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)
