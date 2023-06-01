from .models import Tag, Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields=('__all__')

    def create(self, validated_data):
        instance= Task()
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        if validated_data.get('tags'):
            for tag in validated_data.get('tags'):
                instance.tags.add(tag)
        instance.save()
        return instance
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)
        if validated_data.get('tags'):
            for tag in validated_data.get('tags'):
                instance.tags.add(tag)
        instance.save()
        return instance


