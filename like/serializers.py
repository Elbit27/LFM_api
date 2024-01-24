from rest_framework import serializers
from .models import Like, Favorite



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


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['task_title'] = instance.task.title
        return repr
