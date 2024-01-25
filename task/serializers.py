from rest_framework import serializers
from .models import Task, TaskImage


class TaskListSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Task
        fields = ('id', 'owner', 'owner_username', 'title', 'category', 'category_name',
                  'start_at', 'finish_till', 'place_of_service', 'address', 'phone_number')


class TaskImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = '__all__'


class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    images = TaskImagesSerializer(many=True, required=False)


    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']
        images = request.FILES.getlist('images')
        task = Task.objects.create(**validated_data)
        task_images = [TaskImage(image=image, task=task) for image in images]
        TaskImage.objects.bulk_create(task_images)
        return task


class TaskDetailSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name',)
    images = TaskImagesSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['likes_count'] = instance.likes.count()
        user = self.context['request'].user
        if user.is_authenticated:
            repr['is_liked'] = user.likes.filter(task=instance).exists()
        return repr
