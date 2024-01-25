from rest_framework import serializers
from .models import Respond


class RespondSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Respond
        fields = '__all__'

    def validate(self, attrs):
        user = self.context['request'].user
        task = attrs['task']
        if user.likes.filter(task=task).exists():
            raise serializers.ValidationError(
                "You've already sent respond for this task!"
            )
        return attrs
