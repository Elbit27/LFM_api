from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = '__all__'

    def validate(self, attrs):
        user = self.context['request'].user
        task = attrs['task']
        if user.likes.filter(task=task).exists():
            raise serializers.ValidationError(
                "You already liked this post!"
            )
        return attrs

