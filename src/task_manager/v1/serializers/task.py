from django_filters import OrderingFilter
from rest_framework import serializers

from account.models import User
from task_manager.models import Tasks, Projects, Comments
from task_manager.v1.serializers.comment import CommentSerializer
import django_filters


# class TaskSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     description = serializers.CharField(required=False, allow_blank=True, max_length=255)
#     priority = serializers.IntegerField()
#
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Tasks` instance, given the validated data.
#         """
#         return Tasks.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.priority = validated_data.get("priority", instance.priority)
#         instance.save()
#         return instance




class TaskQueryFilterSerializer(django_filters.FilterSet):
    name__icontains = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    description__icontains = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    priority__gt = django_filters.NumberFilter(field_name='priority', lookup_expr='gt')
    priority__lt = django_filters.NumberFilter(field_name='priority', lookup_expr='lt')
    created_at__gt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at__lt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    ordering = OrderingFilter(
        fields=(
            ('priority','priority'),
            ('created_at','created_at'),
        )
    )

    class Meta:
        model = Tasks
        fields = ['name', 'status','priority','created_at']


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(read_only=True)
    is_reopened = serializers.BooleanField(read_only=True)
    project = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all())
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Tasks
        fields = (
            "id",
            "name",
            "description",
            "priority",
            "is_reopened",
            "status",
            "project",
            "assignee",
            "comments",
        )

    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Task name must be at least 5 characters")
        return value

    def validate(self,attrs):

        name = attrs.get("name")
        assignee = attrs.get("assignee")

        if assignee.is_superuser and len(name) >10:
            raise serializers.ValidationError("Task name must be at least 10 characters and user can not have superuser status")
        return attrs


class TaskUpdateSerializer(serializers.Serializer):
    class Meta:
        model = Tasks
        fields = (
            "name",
            "priority",
        )