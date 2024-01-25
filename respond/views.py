from rest_framework import generics, permissions
from . import serializers


class RespondCreateView(generics.CreateAPIView):
    serializer_class = serializers.RespondSerializer
    permission_classes = [permissions.IsAuthenticated, ]



    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
