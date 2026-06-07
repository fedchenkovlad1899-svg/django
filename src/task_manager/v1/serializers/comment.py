from task_manager.models import Comments

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("id","message")