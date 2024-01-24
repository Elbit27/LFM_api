from rest_framework import generics, permissions
from . import serializers
from .models import Review
from .permissions import IsOwnerOrAdminOrUser

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetailView(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsOwnerOrAdminOrUser(), ]
        return [permissions.AllowAny(), ]
