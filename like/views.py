from rest_framework import generics, permissions
from . import serializers
from .models import Like
from task.permissions import IsOwner


class LikeCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    permission_classes = (IsOwner,)


class FavoriteCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.FavoriteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
