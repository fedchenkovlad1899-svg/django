from django.db.models.signals import post_save
from django.dispatch import receiver
from task_manager.models import Tasks, Comments


@receiver(post_save, sender=Tasks)
def create_task_comment_signal(sender, instance, created, **kwargs):
    if created:
        Comments.objects.create(
            task=instance,
            user=instance.assignee,
            message="Task created"
        )